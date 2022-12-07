class DetailsLevelUsecase:
    def __init__(self, level_service, question_service):
        self.level_service=level_service
        self.questions_service=question_service

    def run(self, id):
        level = self.level_service.detail(id)
        questions = self.questions_service.list_by_level(id)
        
        if level:
            if questions:
                for question in questions:
                    level.questions.append(question.__dict__)
                    pass
            return level.__dict__
        return "level not found"