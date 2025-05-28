from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, count

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("TweetBatchSentiment") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

# Read from MySQL database
df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:mysql://localhost:3306/tweetdb") \
    .option("dbtable", "scored_tweets") \
    .option("user", "sparkuser") \
    .option("password", "Spark@123") \
    .option("driver", "com.mysql.cj.jdbc.Driver") \
    .load()

# Perform sentiment aggregation
agg_df = df.groupBy("sentiment") \
    .agg(
        count("*").alias("tweet_count"),
        avg("polarity").alias("average_polarity")
    )

# Show results in terminal
print("\n=== Sentiment Aggregation Results (Batch Mode) ===")
agg_df.show(truncate=False)

# Optional: Save to CSV if needed
# agg_df.coalesce(1).write.csv("/home/shreya/DBT_PROJECT_cmplt/output/sentiment_summary", header=True, mode="overwrite")

# Stop Spark session
spark.stop()
