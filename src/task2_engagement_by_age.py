from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col

# Create SparkSession with explicit configuration
spark = (SparkSession.builder
    .master("local[*]")
    .appName("EngagementByAgeGroup")
    .config("spark.sql.shuffle.partitions", "4")
    .config("spark.driver.host", "localhost")
    .getOrCreate())

# Load datasets
posts_df = spark.read.option("header", True).csv("input/posts.csv", inferSchema=True)
users_df = spark.read.option("header", True).csv("input/users.csv", inferSchema=True)

# Join posts and users datasets
joined_df = posts_df.join(users_df, "UserID")

# Calculate engagement metrics by age group
engagement_df = (
    joined_df
    .groupBy("AgeGroup")
    .agg(
        avg("Likes").alias("avg_likes"),
        avg("Retweets").alias("avg_retweets")
    )
    .orderBy(col("avg_likes").desc())
)

# Save result
engagement_df.coalesce(1).write.mode("overwrite").csv("outputs/engagement_by_age.csv", header=True)

# Show results
engagement_df.show()

# Stop the SparkSession
spark.stop()