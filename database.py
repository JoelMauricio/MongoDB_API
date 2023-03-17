from pymongo import MongoClient
import os
from dotenv import load_dotenv 
load_dotenv('.env')

string=os.getenv('CLOUD_CONNECTION_STRING')

def get_database():
    client = MongoClient(string)
    db = client[os.getenv('DB_NAME')]
    return db

if __name__ == "__main__":
   dbname= get_database()