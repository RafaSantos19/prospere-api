from App.domain.models.user_model import UserDTO


class CreateUserUsecase:
    def __init__(self, authentication_service, user_service):
        self.user_service=user_service
        self.authentication_service=authentication_service

    def run(self, data):
        user = self.user_service.get_by_email(data['email'])
        if user:
            return "user already exists"
        else:
            encrypted_password = self.authentication_service.encrypt_password(data['password'])
            user = UserDTO(
                name=data['name'],
                email=data['email'],
                password=encrypted_password
            )
            self.user_service.create(user.__dict__)

            return "User sucessufuly created"