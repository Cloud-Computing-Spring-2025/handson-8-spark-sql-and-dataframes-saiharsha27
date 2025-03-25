from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum

# Create SparkSession with explicit configuration
spark = (SparkSession.builder
    .master("local[*]")
    .appName("TopVerifiedUsers")
    .config("spark.sql.shuffle.partitions", "4")
    .config("spark.driver.host", "localhost")
    .getOrCreate())

# Load datasets
posts_df = spark.read.option("header", True).csv("input/posts.csv", inferSchema=True)
users_df = spark.read.option("header", True).csv("input/users.csv", inferSchema=True)

# Join posts and users, filter verified users, calculate total reach
top_verified = (
    posts_df.join(users_df, "UserID")
    .filter(col("Verified") == "True")
    .groupBy("Username")
    .agg(
        (_sum("Likes") + _sum("Retweets")).alias("total_reach")
    )
    .orderBy(col("total_reach").desc())
    .limit(5)
)

# Save result
top_verified.coalesce(1).write.mode("overwrite").csv("outputs/top_verified_users.csv", header=True)

# Show results
top_verified.show()

# Stop the SparkSession
spark.stop()