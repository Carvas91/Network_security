import os
import sys
import json
import pandas as pd

from dotenv import load_dotenv
load_dotenv()
MONGO_DB_URL = os.getenv("MONGO_DB_URL")



import certifi
ca = certifi.where()

import pandas as pd
import numpy as np
import pymongo

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def csv_tojson_convertor(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def push_data_tomongo(self, records, database_name, collection_name):
        try:
            client = pymongo.MongoClient(MONGO_DB_URL)
            db = client[database_name]
            collection = db[collection_name]
            result = collection.insert_many(records)
            return result.inserted_ids
            
        except Exception as e:
            raise NetworkSecurityException(e,sys)


if __name__ == "__main__":
    FILE_PATH = './Network_data/NetworkData.csv'
    DATABASE = 'NetworkDB'
    COLLECTION = 'NetworkData'
    networkobj = NetworkDataExtract()
    records = networkobj.csv_tojson_convertor(FILE_PATH)
    inserted_ids = networkobj.push_data_tomongo(records, DATABASE, COLLECTION)
    print(len(inserted_ids))