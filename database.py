from pymongo import MongoClient
import configuration as C

def get_database():
    client = MongoClient(C.CONNECTION_STRING)
    return client['NOSQL']

if __name__ == "__main__":
    dbname= get_database()