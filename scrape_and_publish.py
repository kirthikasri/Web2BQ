import requests
from bs4 import BeautifulSoup
import json
from google.cloud import pubsub_v1
import os

# Scrape data from the  website
def scrape_converse():
    url = ''
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    list = []
    for item in soup.select('.product-card'):
        shoe = {
            'region': item.select_one('.region').get_text(strip=True),
            'count': item.select_one('.coubt').get_text(strip=True),
        }
        list.append(shoe)
    
    return list

# Publish messages to Pub/Sub
def publish_to_pubsub(data):
    project_id = os.getenv('GCP_PROJECT_ID')
    topic_id = os.getenv('PUBSUB_TOPIC_ID')
    
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_id)
    
    for item in data:
        publisher.publish(topic_path, json.dumps(item).encode('utf-8'))
        print(f'Published message: {item}')

if __name__ == '__main__':
    scraped_data = scrape_converse()
    publish_to_pubsub(scraped_data)
