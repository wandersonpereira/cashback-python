import unittest

from unittest.mock import MagicMock
from src.cashback.actions.login.Post import Post
from src.cashback.crypto.Crypto import Crypto
from src.cashback.crypto.Jwt import Jwt
from src.cashback.adapter.MongoDatabase import MongoDatabase
from src.cashback.client.Client import Client

class Read:
    def read():
        return '{"email": "wanderson.coord@gmail.com", "password": "teste"}'

class Request:
    stream = Read

Client.getClient = MagicMock(return_value=type("MockClient", (), {"database_dev": type("Collection", (), {"reSeller": ""})}))
token: str = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9'

class TestGetLogin(unittest.TestCase):
    def initDatabaseClient(self):
        Client.getClient = MagicMock(return_value=type("MockClient", (), {"database_dev": type("Collection", (), {"reSeller": ""})}))


    def test_valid_user(self):
        self.initDatabaseClient()
        MongoDatabase.get = MagicMock(return_value={"password": "teste", "document": "00033311166"})
        Jwt.encrypt = MagicMock(return_value=token)
        Crypto.isPasswordValid = MagicMock(return_value=True)
        response = Post.execute(Request)
        self.assertEqual(response["data"]["isLogged"], True)
        self.assertEqual(response["data"]["token"], token)

    def test_invalid_password(self):
        self.initDatabaseClient()
        MongoDatabase.get = MagicMock(return_value={"password": "teste", "document": "00033311166"})
        Crypto.isPasswordValid = MagicMock(return_value=False)
        response = Post.execute(Request)
        self.assertEqual(response["data"]["isLogged"], False)

    def test_invalid_user(self):
        self.initDatabaseClient()
        MongoDatabase.get = MagicMock(return_value=None)
        Crypto.isPasswordValid = MagicMock(return_value=False)
        response = Post.execute(Request)
        self.assertEqual(response["data"]["isLogged"], False)

if __name__ == '__main__':
    unittest.main()