import json
from ..actions.cashback.Get import Get
from ..actions.strategy.ControllerAction import ControllerAction

import falcon

class Index(object):

    def on_get(self, req, resp, document):
        response = ControllerAction().execAction(document, Get)
        resp.body = json.dumps(response["data"], ensure_ascii=False)
        resp.status = response["statusCode"] if "statusCode" in response  else falcon.HTTP_200