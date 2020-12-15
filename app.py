import falcon
import router
api = application = falcon.API()
router.builderRouters(api)