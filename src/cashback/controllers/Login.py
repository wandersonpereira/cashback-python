import json
from ..actions.login.Post import Post
from ..actions.strategy.ControllerAction import ControllerAction

import falcon

class Login(object):

    def on_post(self, req, resp):
        response = ControllerAction().execAction(req, Post)
        resp.body = json.dumps(response["data"], ensure_ascii=False)
        resp.status = response["statusCode"] if "statusCode" in response  else falcon.HTTP_200