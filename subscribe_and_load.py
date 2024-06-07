from google.cloud import pubsub_v1
from google.cloud import bigquery
import json
import os

def callback(message):
    print(f'Received message: {message}')
    data = json.loads(message.data)
    insert_into_bigquery(data)
    message.ack()

def insert_into_bigquery(data):
    client = bigquery.Client()
    table_id = os.getenv('BIGQUERY_TABLE_ID')
    
    rows_to_insert = [data]
    
    errors = client.insert_rows_json(table_id, rows_to_insert)
    if errors:
        print(f'Encountered errors while inserting rows: {errors}')
    else:
        print('Rows have been inserted.')

def subscribe():
    project_id = os.getenv('')
    subscription_id = os.getenv('')
    
    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(project_id, subscription_id)
    
    streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
    print(f'Listening for messages on {subscription_path}..\n')
    
    with subscriber:
        try:
            streaming_pull_future.result()
        except TimeoutError:
            streaming_pull_future.cancel()
            streaming_pull_future.result()

if __name__ == '__main__':
    subscribe()
