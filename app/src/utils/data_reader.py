from azure.storage.blob import BlobServiceClient
import pandas as pd
import io
import numpy as np 

def read_data(connection_string:str,blob_name:str,container_name:str,path:str):
    # Initialize the BlobServiceClient
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    # Get the BlobClient
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    # Download the blob's contents as a string
    blob_data = blob_client.download_blob().readall()
    csv_data = pd.read_csv(io.BytesIO(blob_data))
    csv_data.to_csv(path)

def read_data_mock(connection_string:str,blob_name:str,container_name:str,path:str):
    num_rows=100
    np.random.seed(42)
    df=pd.DataFrame()
    random_integers = np.random.randint(1, 11, size=num_rows)
    start_date = pd.to_datetime('2020-01-01')
    end_date = pd.to_datetime('2023-12-31')
    random_dates = pd.to_datetime(np.random.randint(start_date.value, end_date.value, num_rows))
    df["costumer_id"]=range(0,100)
    df["rating"]=random_integers
    df["date"]=random_dates
    df.to_csv(path,index=False)

