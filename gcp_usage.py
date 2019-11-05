from google.cloud import storage

from google.cloud import storage
client = storage.Client()
with open('my_file.dat') as file_obj:
    client.download_blob_to_file('gs://ml-pipeline-playground/shakespeare2.txt', file_obj)