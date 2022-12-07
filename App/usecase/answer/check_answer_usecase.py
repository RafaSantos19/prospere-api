class CheckAnswerUsecase:
    def __init__(self, answer_service):
        self.answer_service = answer_service

    def run(self, question_id, answer_id):
       
        answer = self.answer_service.detail(answer_id)
        if answer:
            if str(answer.question) == question_id:
                return True
            return False
        return None


