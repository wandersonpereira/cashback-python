import unittest
import json
from unittest.mock import MagicMock
import requests as req
from src.cashback.actions.cashback.Get import Get

class ResponseSuccess:
    status_code = 200
    def json():
        return [{"name": "Wanderson"}]

class ResponseEmpty:
    status_code = 201
    def json():
        return []

class ResponseError:
    status_code = 500
    def json():
        return dict(error="Internal Error")

class TestGetCashback(unittest.TestCase):

    def test_request_is_valid(self):
        req.post = MagicMock(return_value=ResponseSuccess)
        response = Get.execute("03011133322")
        self.assertEqual(response["data"][0]["name"], "Wanderson")

    def test_request_document_no_exist(self):
        req.post = MagicMock(return_value=ResponseEmpty)
        response = Get.execute("03011133322")
        self.assertEqual(json.dumps(response["data"]), "[]")

    def test_request_error(self):
        req.post = MagicMock(return_value=ResponseError)
        response = Get.execute("03011133322")
        self.assertEqual(response["data"]["message"], "An error ocurred!")

if __name__ == '__main__':
    unittest.main()