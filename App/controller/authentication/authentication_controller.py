from flask import Response, json
from App.api import Resource

from App.registry.registry import Registry

class AuthenticationController(Resource):
    def __init__(self, api):
        self.api = api
        self.authentication_usecase = Registry().authentication_usecase()

    def post(self):
        data = self.api.payload
        try:
            if data:
                response = self.authentication_usecase.run(data)

                if response:
                    return Response(json.dumps({
                            'user': response
                        }, ensure_ascii=False), status=200)

                return Response(json.dumps({
                        'message': 'Usuário não existe'
                    }, ensure_ascii=False), status=422)    

            return Response(json.dumps({
                    'message': 'Empty data'
                }, ensure_ascii=False), status=400)

        except Exception as ex:
            return Response(json.dumps({
                    'message': str(ex)
                }, ensure_ascii=False), status=500)