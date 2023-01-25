import os
import pymongo

MONGO_DB_URL = os.getenv('MONGO_DB_URL', "mongodb://demo:Joizim9802@127.0.0.1:27017")
DB_NAME = os.getenv('DB_NAME', "twitter-db")
COLLECTION_NAME = os.getenv('COLLECTION_NAME', "tweets")


class MongodbInsert:

    def __init__(self) -> None:

        self.client = pymongo.MongoClient(MONGO_DB_URL)
        self.db_name = DB_NAME
        self.collection_name = COLLECTION_NAME

    def insert_many(self, records):
        self.client[self.db_name][self.collection_name].insert_many(records)

    def insert(self, record):
        self.client[self.db_name][self.collection_name].insert_one(record)


