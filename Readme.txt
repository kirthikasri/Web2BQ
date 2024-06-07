 Scraper to BigQuery

## Description

This project scrapes data from the  website, publishes it to Google Pub/Sub, and then loads it into Google BigQuery.

## Setup

### Prerequisites

1. Python 3.7+
2. Google Cloud SDK installed and initialized
3. Google Cloud project with Pub/Sub and BigQuery APIs enabled

### Installation

1. Clone the repository:
  
    git clone 
    cd -scraper
   

2. Install dependencies:
   
    pip install -r requirements.txt
  

3. Set up Google Cloud authentication:
  
    gcloud auth application-default login
   

4. Set up environment variables:
 
    export GCP_PROJECT_ID='your-gcp-project-id'
    export PUBSUB_TOPIC_ID='your-pubsub-topic-id'
    export PUBSUB_SUBSCRIPTION_ID='your-pubsub-subscription-id'
    export BIGQUERY_TABLE_ID='your-dataset.your-table'


### Running the Scraper

To scrape data and publish it to Pub/Sub:



### running in the bash shell and Deployment in gcloud

python scrape_and_publish.py
python subscribe_and_load.py
