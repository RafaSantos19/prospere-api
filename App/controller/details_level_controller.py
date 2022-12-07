from flask import Response, json
from App.api import Resource

from App.registry.registry import Registry

class DetailsLevelController(Resource):
    def __init__(self, api):
        self.api = api
        self.details_level_usecase = Registry().details_level_usecase()

    def get(self, id):
        try:
            if id:
                response = self.details_level_usecase.run(id)

                if response:
                    return Response(json.dumps({
                            'level': response
                        }, ensure_ascii=False), status=200)

                return Response(json.dumps({
                        'message': 'level not found'
                    }, ensure_ascii=False), status=422)    

            return Response(json.dumps({
                    'message': 'Empty data'
                }, ensure_ascii=False), status=400)

        except Exception as ex:
            return Response(json.dumps({
                    'message': str(ex)
                }, ensure_ascii=False), status=500)