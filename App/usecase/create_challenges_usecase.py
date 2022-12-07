class CreateChallengeUsecase:
    def __init__(self,
        levels_service,
        questions_service,
        answers_service
    ):
        self.levels_service = levels_service
        self.questions_service = questions_service
        self.answers_service = answers_service

    def run(self, data):
        for challenge in data:
            level = self.levels_service.create({ "theme": challenge['theme'], "difficult": challenge['difficult'] })
            
            for question in challenge["questions"]:
                db_question = self.questions_service.create({ "description": question['description'], "points": question['points'], "level": level.id  })

                self.answers_service.create({ "description": question['answer'], "question": db_question.id })
            
        return True