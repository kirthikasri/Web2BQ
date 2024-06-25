#importing the libraries
import requests
from bs4 import BeautifulSoup
import json
from google.cloud import pubsub_v1
import time
import base64
import pandas as pd
import pyarrow


#intializingpub/sub client
project_id=''
topic_id=''
publisher = pubsub_v1.publisherClient()
topic_path = publisher.topic_path(project_id,topic_id)

#intialize bigquery client
client = bigquery.client()


# Scrape data from the  website
def fetch_covid_data():
    url = "https://www.worldometers.info/coronavirus/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data={}
    data['total_cases']=soup.find("div",{"class":"maincounter-number"}).get_txt(strip=True)
    data['deaths']=soup.find_all("div",{"class":"maincounter-number"})[1].get_txt(strip=True)
    data['recovered']=soup.find_all("div",{"class":"maincounter-number"})[2].get_txt(strip=True)
    return data


# Publish messages to Pub/Sub
def publish_to_pubsub(data):
    #coverting the data into json 
    data_str = json.dumps(data)
    #encode the data to bytes
    data_bytes = data_str.encode('utf-8')
    #publish the data to pubsub
    future = publisher.publish(topic_path,data=data_bytes)
    print(f"publish message ID:{future.result()}")



