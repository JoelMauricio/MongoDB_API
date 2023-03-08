from pymongo import MongoClient
import config as C
# from dotenv import load_dotenv 
# load_dotenv('.env')

import os

def get_database():
    # client = MongoClient(os.environ.get('LOCAL_CONNECTION_STRING'))
    # db = client[os.environ.get('DB_NAME')]
    client = MongoClient(C.CLOUD_CONNECTION_STRING)
    db = client[C.DB_NAME]
    return db

if __name__ == "__main__":
   dbname= get_database()