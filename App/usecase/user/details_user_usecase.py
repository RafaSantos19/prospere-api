class DetailsUserUsecase:
    def __init__(self, user_service):
        self.user_service=user_service

    def run(self, id):
        user = self.user_service.details(id)

        if not user:
            return "User not found"
        return user