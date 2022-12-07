class AnswerService:
    def __init__(self, answer_repository):
        self.answer_repository = answer_repository

    def create(self, answer):
        return self.answer_repository.create(answer)

    def detail(self, id):
        return self.answer_repository.detail(id)

    def list_by_level(self, level_id):
        return self.answer_repository.list_by_level(level_id)