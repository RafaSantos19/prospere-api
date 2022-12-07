from flask import Response, json
from App.api import Resource

from App.registry.registry import Registry

class CreateChallengesController(Resource):
    def __init__(self, api):
        self.api = api
        self.create_challenges_usecase = Registry().create_challenges_usecase()

    def post(self):
        data = self.api.payload
        try:
            if data:
                response = self.create_challenges_usecase.run(data["data"])

                if response:
                    return Response(json.dumps({
                            'challenges': response
                        }, ensure_ascii=False), status=201)

                return Response(json.dumps({
                        'message': 'challenger already exist'
                    }, ensure_ascii=False), status=422)    

            return Response(json.dumps({
                    'message': 'Empty data'
                }, ensure_ascii=False), status=400)

        except Exception as ex:
            return Response(json.dumps({
                    'message': str(ex)
                }, ensure_ascii=False), status=500)