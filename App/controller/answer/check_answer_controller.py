from flask import Response, json
from App.api import Resource

from App.registry.registry import Registry

class CheckAnswerController(Resource):
    def __init__(self, api):
        self.api = api
        self.check_answer_usecase = Registry().check_answer_usecase()

    def get(self, id, answer_id):
        try:
            
            response = self.check_answer_usecase.run(id, answer_id)

            if response:
                return Response(json.dumps({
                        'answer': response
                    }, ensure_ascii=False), status=200)

            return Response(json.dumps({
                    'message': 'Resposta incorreta'
                }, ensure_ascii=False), status=422)    

        except Exception as ex:
            return Response(json.dumps({
                    'message': str(ex)
                }, ensure_ascii=False), status=500)