class DetailsQuestionsUsecase:
    def __init__(self, questions_service):
        self.questions_service=questions_service

    def run(self, id):
        questions = self.questions_service.detail(id)

        if questions:
            return questions.__dict__
        return "questions not found"