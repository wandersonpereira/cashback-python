class MongoDatabase(object):

    def __init__(self, table):
        self.table = table
        
    def list(self, key):
        return self.table.find(key)

    def get(self, key):
        return self.table.find_one(key)

    def save(self, item):
        return self.table.insert_one(item)

    def update(self, key, item):
        return self.table.update_one(key, {'$set': item})

    def delete(self, key):
        return self.table.delete_one(key)