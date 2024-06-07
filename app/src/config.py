import os

# Get environment variables
connection_string = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
container_name = os.getenv('CONTAINER_NAME')
blob_name = os.getenv('BLOB_NAME')
