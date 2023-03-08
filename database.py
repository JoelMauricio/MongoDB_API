from pymongo import MongoClient
from dotenv import load_dotenv 
load_dotenv('.env')

import os

#def get_database():
client = MongoClient(os.environ.get('LOCAL_CONNECTION_STRING'))
db = client['restaurants']
    #return client['NOSQL']

#if __name__ == "__main__":
#    dbname= get_database()