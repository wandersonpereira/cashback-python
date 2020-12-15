import unittest

from unittest.mock import MagicMock
from src.cashback.actions.order.Get import Get
from src.cashback.actions.order.rules.Bonus import Bonus
from src.cashback.adapter.MongoDatabase import MongoDatabase
from src.cashback.client.Client import Client
import datetime

class Read:
    def read():
        return '{"email": "wanderson.coord@gmail.com", "password": "teste"}'

class Request:
    stream = Read
    def get_header(value):
        return ""

Client.getClient = MagicMock(return_value=type("MockClient", (), {"database_dev": type("Collection", (), {"order": ""})}))

class TestGetLogin(unittest.TestCase):
    def initDatabaseClient(self):
        Client.getClient = MagicMock(return_value=type("MockClient", (), {"database_dev": type("Collection", (), {"order": ""})}))

    def test_list_order(self):
        self.initDatabaseClient()
        MongoDatabase.list = MagicMock(return_value=[
            {"_id": "123", "value": 15.00, "date": datetime.datetime.utcnow()},
            {"_id": "124", "value": 200.00, "date": datetime.datetime.utcnow()},
        ])

        Bonus.getPercent = MagicMock(return_value=10)

        response = Get.execute(Request)
        self.assertEqual(response["data"][0]["percent"], 10)
        self.assertEqual(response["data"][0]["value"], 15.00)
        self.assertEqual(response["data"][0]["_id"], "123")

        self.assertEqual(response["data"][1]["percent"], 10)
        self.assertEqual(response["data"][1]["value"], 200.00)
        self.assertEqual(response["data"][1]["_id"], "124")


    def test_none_order(self):
        self.initDatabaseClient()
        MongoDatabase.list = MagicMock(return_value=None)

        response = Get.execute(Request)
        self.assertEqual(len(response["data"]), 0)

if __name__ == '__main__':
    unittest.main()