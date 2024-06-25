

def pubsub_to_bigquery(event,context):
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    data = json.loads(pubsub_message)
    #create a row to insert  
    rows_to_insert = [
        {
            "total_cases": data['total_cases'],
            "deaths":data['deaths'],
            "recovered":data['recovered']
        }
        
    ]
    
    df = pd.Dataframe(rows_to_insert)
    table = pyarrow.Table.from_pandas(df)
    table_id ='project_id.my_dataset.covid_data'
    df['total_cases'] = df['total_cases'].astype(str)
    df['deaths'] = df['deaths'].astype(str)
    df['recovered'] = df['recovered'].astype(str)
    
    job = client.load_table_from_dataframe(df,table_id)
    
    


def main():
    covid_data = fetch_covid_data()
    print(f"Fetched Data: {covid_data}")
    publish _to_pubsub(covid_data)
    pubsub_message = {
        'data':base64.b6encode(json.dumps(covid_data).encode('utf-8')).decode('utf-8')
    }
    pubsub_to_bigquery(pubsub_message,None)

if __name__ == "__main__":
    main()
