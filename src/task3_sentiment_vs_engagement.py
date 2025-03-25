from pyspark.sql import SparkSession
from pyspark.sql.functions import when, avg, col

# Create SparkSession with explicit configuration
spark = (SparkSession.builder
    .master("local[*]")
    .appName("SentimentVsEngagement")
    .config("spark.sql.shuffle.partitions", "4")
    .config("spark.driver.host", "localhost")
    .getOrCreate())

# Load posts data
posts_df = spark.read.option("header", True).csv("input/posts.csv", inferSchema=True)

# Categorize sentiment
sentiment_stats = (
    posts_df
    .withColumn(
        "sentiment_category", 
        when(col("SentimentScore") > 0.3, "Positive")
        .when(col("SentimentScore") < -0.3, "Negative")
        .otherwise("Neutral")
    )
    .groupBy("sentiment_category")
    .agg(
        avg("Likes").alias("avg_likes"),
        avg("Retweets").alias("avg_retweets")
    )
    .orderBy(col("avg_likes").desc())
)

# Save result
sentiment_stats.coalesce(1).write.mode("overwrite").csv("outputs/sentiment_engagement.csv", header=True)

# Show results
sentiment_stats.show()

# Stop the SparkSession
spark.stop()