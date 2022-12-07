class ListLevelsUsecase:
    def __init__(self, level_service):
        self.level_service = level_service

    def run(self):    
        levels = self.level_service.list()
        if levels:

            list_levels = []

            for level in levels:
                list_levels.append(level.__dict__)
            return list_levels
        return None


