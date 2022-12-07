class DetailsLevelUsecase:
    def __init__(self, level_service):
        self.level_service=level_service

    def run(self, id):
        level = self.level_service.details(id)

        if not level:
            return "level not found"
        return level