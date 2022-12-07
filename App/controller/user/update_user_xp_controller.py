from flask import Response, json
from App.api import Resource

from App.registry.registry import Registry

class UpdateUserXPController(Resource):
    def __init__(self, api):
        self.api = api
        self.update_user_xp_usecase = Registry().update_user_xp_usecase()

    def put(self, id, xp):
        try:
            if xp:
                response = self.update_user_xp_usecase.run(id, xp)

                if response:
                    return Response(json.dumps({
                            'user': response
                        }, ensure_ascii=False), status=200)

                return Response(json.dumps({
                        'message': 'user not found'
                    }, ensure_ascii=False), status=422)    

            return Response(json.dumps({
                    'message': 'Empty data'
                }, ensure_ascii=False), status=400)

        except Exception as ex:
            return Response(json.dumps({
                    'message': str(ex)
                }, ensure_ascii=False), status=500)