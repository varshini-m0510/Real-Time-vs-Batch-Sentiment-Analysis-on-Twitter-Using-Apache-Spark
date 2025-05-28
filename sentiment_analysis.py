from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, regexp_replace, udf, col
from pyspark.sql.types import FloatType, StringType
from textblob import TextBlob

# Sentiment analysis using TextBlob
def get_polarity(text):
    return TextBlob(text).sentiment.polarity

def get_subjectivity(text):
    return TextBlob(text).sentiment.subjectivity

def get_sentiment_label(score):
    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"

# Register UDFs
polarity_udf = udf(get_polarity, FloatType())
subjectivity_udf = udf(get_subjectivity, FloatType())
sentiment_label_udf = udf(get_sentiment_label, StringType())

# Initialize Spark
spark = SparkSession.builder \
    .appName("RealTimeTweetSentiment") \
    .getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

# Read streaming data from socket
lines = spark.readStream \
    .format("socket") \
    .option("host", "localhost") \
    .option("port", 5555) \
    .load()

# Extract tweets using custom delimiter
tweets = lines.select(explode(split(col("value"), "t_end")).alias("value"))

# Clean text
cleaned = tweets.withColumn("cleaned_text", regexp_replace("value", r"http\S+|@\S+|#|\n", ""))

# Apply TextBlob-based sentiment functions
scored = cleaned.withColumn("polarity", polarity_udf(col("cleaned_text"))) \
                .withColumn("subjectivity", subjectivity_udf(col("cleaned_text"))) \
                .withColumn("sentiment", sentiment_label_udf(col("polarity")))

# Show full detailed output in the console
query = scored.writeStream \
    .outputMode("append") \
    .format("console") \
    .option("truncate", False) \
    .start()

query.awaitTermination()

