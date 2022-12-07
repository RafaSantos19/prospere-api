class ListAnswerUsecase:
    def __init__(self, answer_service, question_service):
        self.answer_service = answer_service
        self.question_service = question_service

    def run(self, id):
        question = self.question_service.detail(id)

        if question:
            answers = self.answer_service.list_by_level(question.level)
            if answers:
                list_answers = []
                for answer in answers:
                    list_answers.append(answer.__dict__)
                return list_answers
        return None


