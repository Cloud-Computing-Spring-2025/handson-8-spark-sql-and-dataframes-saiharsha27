from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, col, count

# Create SparkSession with explicit configuration
spark = (SparkSession.builder
    .master("local[*]")  # Use all available cores
    .appName("HashtagTrends")
    .config("spark.sql.shuffle.partitions", "4")  # Reduce shuffle partitions for small data
    .config("spark.driver.host", "localhost")  # Explicitly set driver host
    .getOrCreate())

# Load posts data
posts_df = spark.read.option("header", True).csv("input/posts.csv")

# Split the Hashtags column into individual hashtags and count the frequency of each hashtag
hashtag_counts = (
    posts_df
    .select(explode(split(col("Hashtags"), ",")).alias("hashtag"))
    .groupBy("hashtag")
    .agg(count("*").alias("count"))
    .orderBy(col("count").desc())
    .limit(10)
)

# Save result
hashtag_counts.coalesce(1).write.mode("overwrite").csv("outputs/hashtag_trends.csv", header=True)

# Show results
hashtag_counts.show()

# Stop the SparkSession
spark.stop()