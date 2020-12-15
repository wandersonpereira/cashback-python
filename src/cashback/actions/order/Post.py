import json
from .models.OrderModel import  OrderModel
from .rules.Status import Status
from src.cashback.adapter.MongoDatabase import MongoDatabase
from src.cashback.client.Client import Client

class Post():

    def execute(request): 
        model = OrderModel().load(json.load(request.stream))
        model["status"] = Status.getStatus(model)
        client = Client().getClient()
        database = MongoDatabase(client.database_dev.order)
        orderCreated = database.save(model)

        return {"data": {"orderId": str(orderCreated.inserted_id)}}