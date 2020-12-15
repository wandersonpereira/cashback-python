from src.cashback.adapter.Logger import Logger
import src.cashback.types.Error as Error

class ControllerAction():

    def execAction(self, request, action):
        try:
            return action.execute(request)
        except Exception as e:
            Logger().error(e)
            return {
                "data": {"message": Error.INTERNAL_ERROR},
                "statusCode": "500"
            }
       