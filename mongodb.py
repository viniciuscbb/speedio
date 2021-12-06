from pymongo import MongoClient
import urllib

username = urllib.parse.quote_plus('')
password = urllib.parse.quote_plus('')
collection  = MongoClient(f'mongodb+srv://{username}:{password}@ip')

class MongoDB:
    def __init__(self):
        self.db = collection['speedio']['estabelecimentos']

    def insertMany(self, data):
        self.db.insert_many(data)

    def insert(self, data):
        self.db.insert_one(data)

    def find(self, data):
        return self.db.find(data)

    def find_one(self, data):
        return self.db.find_one(data)
