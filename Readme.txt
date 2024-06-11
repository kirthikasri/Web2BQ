Scraper to BigQuery

This project scrapes the data from a website, publishes it into Google Pub/Sub, and then loads it into Google BigQuery
#Setup
#Prerequisites
Python 3.7
Google Cloud SDK installed and initialized
Google Cloud project with Pub/Sub and BigQuery APIs enabled
#Installation
1.Clone the repository
2.Install dependencies
3.Set up Google Cloud authentication
4.Set up environment variables
export GCP_PROJECT_ID=''
export PUBSUB_TOPIC_ID=''
export PUBSUB_SUBSCRIPTION_ID=''
export BIGQUERY_TABLE_ID=''
#Running the Scraper
To scrape data and publish it to Pub/Sub
python scrape_and_publish.py
#Running in the Bash Shell and Deployment in GCloud
To subscribe to the Pub/Sub topic and load data into BigQuery
python subscribe_and_load.py
