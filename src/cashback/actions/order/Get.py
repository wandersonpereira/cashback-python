import json
from itertools import groupby
from pymongo import MongoClient
from src.cashback.adapter.MongoDatabase import MongoDatabase
from src.cashback.client.Client import Client
from src.cashback.crypto.Jwt import Jwt
from .rules.Bonus import  Bonus


class Get():
    
    def execute(request): 
        reSeller = Jwt().decrypt(request.get_header("Authorization"))
        client = Client().getClient()
        database = MongoDatabase(client.database_dev.order)
        cursor = database.list({"document": reSeller["document"]})
        data = []

        if cursor != None:
            for key, value in groupby(list(cursor), Bonus().getGroupToCalcPercente):
                orders = list(value)
                percentualBunus = Bonus().getPercentBonus(sum(row["value"] for row in orders))

                x = map(lambda x: dict(x, **{
                    "_id": str(x["_id"]),
                    "date": str(x["date"]),
                    "percent": percentualBunus
                }), orders)

                data = data + list(x)

        return {"data": data}