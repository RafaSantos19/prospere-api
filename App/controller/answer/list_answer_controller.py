from flask import Response, json
from App.api import Resource

from App.registry.registry import Registry

class ListAnswerController(Resource):
    def __init__(self, api):
        self.api = api
        self.list_answer_usecase = Registry().list_answer_usecase()

    def get(self, id):
        try:
            response = self.list_answer_usecase.run(id)
            if response:
                return Response(json.dumps({
                        'answer': response
                    }, ensure_ascii=False), status=200)

            return Response(json.dumps({
                    'message': 'Nenhuma resposta encontrada'
                }, ensure_ascii=False), status=422)    

        except Exception as ex:
            return Response(json.dumps({
                    'message': str(ex)
                }, ensure_ascii=False), status=500)