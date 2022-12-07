class AuthenticationUsecase:
    def __init__(self, authentication_service, user_service):
        self.user_service=user_service
        self.authentication_service=authentication_service

    def run(self, data):
        try:
            user = self.user_service.get_by_email(data['email'])
            if user:
                user_pwd = self.user_service.get_access(user.id)
                access = self.authentication_service.authentication_access(user_pwd, data['password'])
                if access:
                    # return self.authentication_service.generator_token_access(
                    #     {
                    #         "id": user.id,
                    #         "name": user.name,
                    #         "email": user.email,
                    #         "xp": user.xp
                    #     })
                    return { "id": user.id, "name": user.name, "email": user.email, "xp": user.xp }
                    
            raise Exception("usuário ou não senha conferem")
        except Exception as ex:
            raise ex
            