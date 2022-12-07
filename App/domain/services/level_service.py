class LevelService:
    def __init__(self, level_repository):
        self.level_repository = level_repository

    def create(self, level):
        return self.level_repository.create(level)

    def detail(self, id):
        return self.level_repository.detail(id)

    def list(self):
        return self.level_repository.list()
    
    def list_by_difficult(self, difficult):
        target = self.level_repository.list()

        levels = list(filter(lambda l: l.difficult==difficult), target)
        return levels