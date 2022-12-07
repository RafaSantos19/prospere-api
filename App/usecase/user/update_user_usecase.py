class UpdateUserUsecase:
    def __init__(self, user_service, authentication_service):
        self.user_service = user_service
        self.authentication_service = authentication_service
    def run(self, id, data):

        if data.get("password"):
            encrypted_password = self.authentication_service.encrypt_password(data['password'])
            data["password"] = encrypted_password

        user = self.user_service.update(id, data)


        if not user:
            return None
        return user