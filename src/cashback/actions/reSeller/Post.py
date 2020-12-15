import json
from .models.ReSellerModel import  ReSellerModel
from src.cashback.adapter.MongoDatabase import MongoDatabase
from src.cashback.client.Client import Client
from src.cashback.crypto.Crypto import Crypto

class Post():
    
    def execute(request): 
        model = ReSellerModel().load(json.load(request.stream))
        model["password"] = Crypto().encrypt(model["password"])
        client = Client().getClient()
        database = MongoDatabase(client.database_dev.reSeller)
        sellerCreated = database.save(model)
        return {"data": {"sellerId": str(sellerCreated.inserted_id)}}