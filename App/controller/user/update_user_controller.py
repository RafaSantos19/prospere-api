from flask import Response, json
from App.api import Resource

from App.registry.registry import Registry

class UpdateUserController(Resource):
    def __init__(self, api):
        self.api = api
        self.update_user_usecase = Registry().update_user_usecase()

    def put(self, id):
        data = self.api.payload
        try:
            if data:
                response = self.update_user_usecase.run(id, data)

                if response:
                    return Response(json.dumps({
                            'user': response
                        }, ensure_ascii=False), status=200)

                return Response(json.dumps({
                        'message': 'user already existse'
                    }, ensure_ascii=False), status=422)    

            return Response(json.dumps({
                    'message': 'Empty data'
                }, ensure_ascii=False), status=400)

        except Exception as ex:
            return Response(json.dumps({
                    'message': str(ex)
                }, ensure_ascii=False), status=500)
            
            
            