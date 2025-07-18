import os
import json
import sys
import certifi
import pandas as pd
from dotenv import load_dotenv
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException
import pymongo

load_dotenv()
url = os.getenv('MONGO_URL')
ca = certifi.where()

class NetworkDataExtract():
    def __init__(self, database, collection):
        try:
            self.mongo_client = pymongo.MongoClient(url)
            self.database = self.mongo_client[database]
            self.collection = self.database[collection]
        
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def csv_to_json_converter(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_mongo(self, records):
        try:
            self.collection.insert_many(records)
            return f"{len(records)} new records inserted successfully."
        except Exception as e:
            raise NetworkSecurityException(e, sys)


if __name__ == "__main__":
    FILE_PATH = 'Network_Data/phisingData.csv'
    DATABASE = 'MAHAVEER_DB'
    COLLECTION = "NetworkData"

    network_obj = NetworkDataExtract(DATABASE, COLLECTION)
    records = network_obj.csv_to_json_converter(FILE_PATH)
    # print(network_obj.insert_data_mongo(records))
