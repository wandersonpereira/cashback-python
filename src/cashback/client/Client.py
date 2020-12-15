from pymongo import MongoClient

class Client(object):
    def getClient(self):
        return MongoClient('mongodb://mongoadmin:secret@172.168.0.11:27017')