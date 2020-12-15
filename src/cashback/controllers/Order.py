import json
from ..actions.order.Post import Post
from ..actions.order.Get import Get
from ..actions.strategy.ControllerAction import ControllerAction

import falcon

class Order(object):

    def on_get(self, req, resp):
        response = ControllerAction().execAction(req, Get)
        resp.body = json.dumps(response["data"], ensure_ascii=False)
        resp.status = response["statusCode"] if "statusCode" in response  else falcon.HTTP_200

    def on_post(self, req, resp):
        response = ControllerAction().execAction(req, Post)
        resp.body = json.dumps(response["data"], ensure_ascii=False)
        resp.status = response["statusCode"] if "statusCode" in response  else falcon.HTTP_200
