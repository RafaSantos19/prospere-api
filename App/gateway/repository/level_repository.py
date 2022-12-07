from App.gateway.database.database_models import Levels
from App.domain.models.level_model import LevelDTO

class LevelRepository:
    def __init__(self, conn):
        self.conn = conn

    def create(self, level):
        try:
            db_level = Levels()
            db_level.theme = level['theme']
            db_level.difficult = level['difficult']

            self.conn.add(db_level)
            self.conn.flush()
            self.conn.refresh(db_level)
            self.conn.commit()

            return LevelDTO(
                id=db_level.id,
                theme=db_level.theme,
                difficult=db_level.difficult,
            )
        except Exception as ex:
            raise ex
        finally:
            self.conn.close()

    def detail(self, id):
        try:
            db_level = self.conn.query(Levels).get(id)

            if db_level:
                return LevelDTO(
                    id=db_level.id,
                    theme=db_level.theme,
                    difficult=db_level.difficult,
                )
        except Exception as ex:
            raise ex
        finally:
            self.conn.close()  

    def list(self):
        try:
            db_levels = self.conn.query(Levels).all()
            list_dto = []

            if db_levels:
                for level in db_levels:
                    list_dto.append(
                        LevelDTO(
                            id=level.id,
                            theme=level.theme,
                            difficult=level.difficult,
                        ))
                return list_dto        
        except Exception as ex:
            raise ex
        finally:
            self.conn.close()
