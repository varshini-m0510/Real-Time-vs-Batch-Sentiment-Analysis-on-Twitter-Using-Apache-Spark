# Real-Time-vs-Batch-Sentiment-Analysis-on-Twitter-Using-Apache-Spark

This project demonstrates a complete sentiment analysis pipeline on Twitter data using both batch and real-time streaming methods. It leverages Apache Spark, Kafka, and MySQL to process, analyze, and store the sentiment of tweets in near real-time and compare it with batch-mode performance.

## 📌 Features

- Real-time tweet ingestion using Twitter API and Kafka
- Batch tweet collection and processing
- Sentiment classification of tweets using Spark
- MySQL database integration for result storage
- Comparative analysis between batch and streaming modes

## 🛠️ Technologies Used

- Python
- Apache Spark (Streaming + Batch)
- Apache Kafka
- Twitter Developer API
- MySQL
- JDBC Connector (MySQL)

## 📂 Project Structure
├── twitter_streamer.py # Real-time tweet streaming (Kafka producer)

├── twitter_producer.py # Alternate tweet producer

├── twitter_batch.py # Batch tweet collection

├── spark_streaming_sentiment.py # Spark streaming sentiment analysis

├── batch_sentiment_analysis.py # Batch mode sentiment analysis

├── sentiment_analysis.py # Core sentiment logic

├── evaluate_streaming.py # Streaming evaluation

├── compare_results.py # Batch vs streaming results

├── mysql-connector-j-* # MySQL JDBC connectors

├── commands.txt # Useful CLI commands
