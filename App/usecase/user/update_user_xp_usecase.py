class UpdateUserXPUsecase:
    def __init__(self, user_service):
        self.user_service=user_service

    def run(self, id, xp):
        user = self.user_service.update_xp(id, xp)

        if not user:
            return None
        return user