from datetime import datetime


class AuthenticationService:
    def __init__(self, secutiry) -> None:
        self.secutiry=secutiry

    def encrypt_password(self, password):
        return self.secutiry.encrypt_password(password)

    def authentication_access(self, user_pass, password):
        return user_pass == self.secutiry.authentication_access(password)

    def generator_token_access(self, user):
        return self.secutiry.generator_token_access(user)

    def athentication_token_access(self, token):
        decode = self.secutiry.athentication_token(token)
        return datetime.timestamp(datetime.now()) - datetime.timestamp(decode['exp']) < 7200