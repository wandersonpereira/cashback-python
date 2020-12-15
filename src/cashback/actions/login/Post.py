import json

from .models.LoginModel import  LoginModel
from src.cashback.adapter.MongoDatabase import MongoDatabase
from src.cashback.client.Client import Client
from src.cashback.crypto.Crypto import Crypto
from src.cashback.crypto.Jwt import Jwt

class Post():
    
    def execute(request): 
        model = LoginModel().load(json.load(request.stream))
        client = Client().getClient()
        database = MongoDatabase(client.database_dev.reSeller)
        seller = database.get({"email": model["email"]})

        if seller != None:
            return {
                "data": {
                    "isLogged": Crypto().isPasswordValid(model["password"], seller["password"]),
                    "token": str(Jwt().encrypt({"document": seller["document"]}))
                }
            }

        return {"data": {"isLogged": False}, "statusCode": "401"}
            
