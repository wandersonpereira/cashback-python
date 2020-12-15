from src.cashback.controllers.Index import Index
from src.cashback.controllers.ReSeller import ReSeller
from src.cashback.controllers.Order import Order
from src.cashback.controllers.Login import Login

def builderRouters(api): 
    api.add_route('/login', Login())
    api.add_route('/reseller', ReSeller())
    api.add_route('/order', Order())
    api.add_route('/cashback/{document:int(11)}', Index())