from App.gateway.database.database_models import Users
from App.domain.models.user_model import UserDTO

class UserRepository:
    def __init__(self, conn):
        self.conn = conn

    def create(self, user):
        try:
            db_user=Users()
            db_user.name = user['name']
            db_user.email = user['email']
            db_user.password = user['password']

            self.conn.add(db_user)
            self.conn.flush()
            self.conn.refresh(db_user)
            self.conn.commit()

            return UserDTO(
                id=db_user.id,
                name=db_user.name,
                email=db_user.email,
                xp=db_user.xp
            )
        except Exception as ex:
            raise ex
        finally:
            self.conn.close()

    def update(self, id, user):
        try:
            db_user=Users()
            # db_user.id = id
            # db_user.name = user['name']
            # db_user.email = user['email']
            # db_user.password = user['password']
            # db_user.xp = user['xp']

            self.conn.query(Users).filter(Users.id == id).update(user, synchronize_session='evaluate')
            self.conn.flush()
            self.conn.commit()

            return True

        except Exception as ex:
            raise ex
        finally:
            self.conn.close()

    def update_xp(self, id, xp):
        try:
            self.conn.query(Users).filter(Users.id == id).update({"xp": xp}, synchronize_session='evaluate')
            self.conn.flush()
            self.conn.commit()

            return xp

        except Exception as ex:
            raise ex
        finally:
            self.conn.close()

    def detail(self, id):
        db_user = self.__get_by_id(id)

        if db_user:
            return UserDTO(
                    id=db_user.id,
                    name=db_user.name,
                    email=db_user.email,
                    xp=db_user.xp
                )


    def get_user_access(self, id):
        db_user = self.__get_by_id(id)

        if db_user:
            return db_user.password

    def get_by_email(self, email):
        try:
            db_user = self.conn.query(Users).filter_by(email=email).first()

            if db_user:
                return UserDTO(
                    id=db_user.id,
                    name=db_user.name,
                    email=db_user.email,
                    xp=db_user.xp
                )
            return None

        except Exception as ex:
            raise ex
        finally:
            self.conn.close()

    def delete(self, id):
        try:
            self.conn.query(Users).delete(Users.id == id)
            return True

        except Exception as ex:
            raise ex
        finally:
            self.conn.close()


    def __get_by_id(self, id):
        try:
            db_user = self.conn.query(Users).get(id)

            if db_user:
                return db_user

        except Exception as ex:
            raise ex
        finally:
            self.conn.close()        