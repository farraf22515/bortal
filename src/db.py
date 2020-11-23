import pymongo
import os
from os.path import join, dirname
from dotenv import load_dotenv

# dotenv_path = join(dirname(__file__), '.env')
# load_dotenv(dotenv_path)
ID = os.environ["ID"]
PASSWORD = os.environ["PASSWORD"]


class DB:
    URI = f'mongodb+srv://{ID}:{PASSWORD}@cluster0.4hy63.mongodb.net/SW-project?retryWrites=true&w=majority'

    @staticmethod
    def init():
        client = pymongo.MongoClient(DB.URI)
        DB.DATABASE = client["SW-project"]
        print("Database success")

    @staticmethod
    def insertInto(collection, data):
        DB.DATABASE[collection].insert(data)

    @staticmethod
    def listAllCol(collection):
        return DB.DATABASE[collection].find()

    @staticmethod
    def listCol(collection, query):
        return DB.DATABASE[collection].find(query)

    @staticmethod
    def updateCol(collection, where, query):
        DB.DATABASE[collection].update(where, query)
