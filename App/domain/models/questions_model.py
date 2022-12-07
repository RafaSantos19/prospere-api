class QuestionDTO:
    def __init__(self, id="", description="", points="", level="", answer=None):
        self.id = id
        self.description = description
        self.points = points
        self.level = level
        self.answer = [] if answer is None else answer