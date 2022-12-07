from App.gateway.database.database_models import Base

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import SingletonThreadPool

from config import Config

class Database:
    engine = None
    _SessionFactory = None

    def __init__(self):
        self.engine = create_engine(Config.DATABASE_URL, echo=False, poolclass=SingletonThreadPool,  connect_args={"check_same_thread": False})
        self._SessionFactory = sessionmaker(autocommit=False, bind=self.engine)
        self.Base = Base

    def session_factory(self):
        self.Base.metadata.create_all(self.engine)
        return self._SessionFactory()        