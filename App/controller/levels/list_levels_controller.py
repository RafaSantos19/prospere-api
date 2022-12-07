from flask import Response, json
from App.api import Resource

from App.registry.registry import Registry

class ListLevelsController(Resource):
    def __init__(self, api):
        self.api = api
        self.list_levels_usecase = Registry().list_levels_usecase()

    def get(self):
        try:
            
            response = self.list_levels_usecase.run()

            if response:
                return Response(json.dumps({
                        'levels': response
                    }, ensure_ascii=False), status=200)

            return Response(json.dumps({
                    'message': 'Nenhum nivel encontrado'
                }, ensure_ascii=False), status=422)    

        except Exception as ex:
            return Response(json.dumps({
                    'message': str(ex)
                }, ensure_ascii=False), status=500)