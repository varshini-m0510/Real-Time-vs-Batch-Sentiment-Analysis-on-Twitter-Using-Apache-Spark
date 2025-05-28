import time
import mysql.connector

start_time = time.time()

# Simulate streaming already running (via twitter_producer.py + spark streaming)
print("Waiting 60 seconds for streaming mode to populate MySQL...")
time.sleep(60)  # Let streaming mode populate tweets

# Connect to MySQL and query results
conn = mysql.connector.connect(
    host="localhost",
    user="sparkuser",
    password="Spark@123",
    database="tweetdb"
)
cursor = conn.cursor()

cursor.execute("""
    SELECT sentiment, COUNT(*) as tweet_count, AVG(polarity) as average_polarity
    FROM scored_tweets
    GROUP BY sentiment;
""")
streaming_results = cursor.fetchall()

print("\n=== STREAMING MODE RESULTS ===")
for row in streaming_results:
    print(f"Sentiment: {row[0]}, Count: {row[1]}, Avg Polarity: {row[2]}")

end_time = time.time()
print(f"\n⏱️ Streaming Mode Execution Time (including wait): {end_time - start_time:.2f} seconds")

cursor.close()
conn.close()
