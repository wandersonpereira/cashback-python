import unittest

from unittest.mock import MagicMock
from src.cashback.actions.reSeller.Post import Post
from src.cashback.crypto.Crypto import Crypto
from src.cashback.crypto.Jwt import Jwt
from src.cashback.adapter.MongoDatabase import MongoDatabase
from src.cashback.client.Client import Client

class Read:
    def read():
        return '{"fullName": "Wanderson", "document": "0003331122", "email": "wanderson.coord@gmail.com", "password": "teste"}'

class Request:
    stream = Read

class ResponseSave:
    inserted_id = "123456789123456"


class TestGetLogin(unittest.TestCase):
    def initDatabaseClient(self):
        Client.getClient = MagicMock(return_value=type("MockClient", (), {"database_dev": type("Collection", (), {"reSeller": ""})}))

    def test_create_reseller(self):
        self.initDatabaseClient()
        MongoDatabase.save = MagicMock(return_value=ResponseSave)
        Crypto.encrypt = MagicMock(return_value="ttdsfd55ga55sdg4")
        response = Post.execute(Request)

        self.assertEqual(response["data"]["sellerId"], "123456789123456")

if __name__ == '__main__':
    unittest.main()