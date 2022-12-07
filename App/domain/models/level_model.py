class LevelDTO:
    def __init__(self, id="", theme="", difficult="", questions=None):
        self.id=id
        self.theme=theme
        self.difficult=difficult
        self.questions= [] if questions is None else questions