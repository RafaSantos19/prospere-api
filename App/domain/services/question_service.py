class QuestionsService:
    def __init__(self, questions_repository):
        self.questions_repository = questions_repository

    def create(self, question):
        return self.questions_repository.create(question)

    def detail(self, id):
        return self.questions_repository.detail(id)
   
    def list_by_level(self, level):
        return self.questions_repository.list(level)