<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
   
</head>
<body>
    <h2>Scraper to BigQuery</h2>
    <p>This project scrapes the data from a website and publishes it into Google Pub/Sub and then loads it into Google BigQuery.</p>
<h3></h3>
    <h3><b>Setup</b></h3>
    <h3>Requirements</h3>
    <ul>
        <li>Python 3.7</li>
        <li>Google Cloud SDK installed and initialized</li>
        <li>Google Cloud project with Pub/Sub and BigQuery APIs enabled</li>
    </ul>
<h3>Installation</h3>
    <ol>
        <li>Clone the repository</li>
        <li>Install dependencies</li>
        <li>Set up Google Cloud authentication</li>
        <li>Set up environment variables</li>
    </ol>
    <pre>
        export GCP_PROJECT_ID
        export PUBSUB_TOPIC_ID
        export BIGQUERY_TABLE_ID
    </pre>
  <h3>Running the Scraper</h3>
    <p>To scrape data and publish it to Pub/Sub:</p>
    <pre>
        python scrape_and_publish.py
    </pre>

   <h3>Pushing the data in GCloud BigQuery</h3>
   <p>To load data into BigQuery:</p>
    <pre>
        pubsub_to_bigquery(pubsub_message)
    </pre>
</body>
</html>
