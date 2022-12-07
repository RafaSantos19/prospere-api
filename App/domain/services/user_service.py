from copy import deepcopy


class UserService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def create(self, user):
        return self.user_repository.create(user)

    def update(self, id, user):
        db_user = self.user_repository.detail(id)

        if not db_user:
            return "user not found"
        
        else:
            db_user = db_user.__dict__
            for key, value in user.items():
                db_user[key] = value 
            _copy = deepcopy(db_user)
            for key, value in _copy.items():
                if not value:
                    db_user.pop(key)    
            return self.user_repository.update(id, db_user)

    def update_xp(self, id, xp):
        db_user = self.user_repository.detail(id)

        if not db_user:
            return "user not found"
        
        else:
            return self.user_repository.update_xp(id, xp)

    def delete(self, id):
        db_user = self.user_repository.detail(id)

        if not db_user:
            return "user not found"
        
        else:
            return self.user_repository.delete(id)

    def details(self, id):
        db_user = self.user_repository.detail(id)

        if not db_user:
            return "user not found"
        
        else:
            return db_user.__dict__

    def get_by_email(self, email):
        db_user = self.user_repository.get_by_email(email)
        
        if not db_user:
            return None
        
        else:
            return db_user

    def get_access(self, id):
        return self.user_repository.get_user_access(id)