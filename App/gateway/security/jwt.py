import jwt
from datetime import datetime

class JWT:
    def __init__(self, config):
        self.config=config

    def encrypt_password(self, password):
        encoded = jwt.encode({"pass": password}, self.config.SECRET, algorithm="HS256")
        return encoded

    def authentication_access(self, password):
        return jwt.encode({"pass": password}, self.config.SECRET, algorithm="HS256")

    def generator_token_access(self, user):
        return jwt.encode({"user": user, "exp": datetime.timestamp(datetime.now())}, self.config.SECRET, algorithm="HS256")

    def athentication_token_access(self, token):
        decoded = jwt.decode(token, self.config.SECRET, algorithms=["HS256"])
        return decoded