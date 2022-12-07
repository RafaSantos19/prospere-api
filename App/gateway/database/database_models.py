from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    email = Column(String)
    password = Column(String)
    xp = Column(Integer)
    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, email={self.email!r}, xp={self.xp!r})"

class Levels(Base):
    __tablename__ = "levels"
    id = Column(Integer, primary_key=True)
    difficult = Column(String(30))
    theme = Column(String)
    # question = relationship("Questions", back_populates='level', cascade='all, delete-orphan')
    def __repr__(self):
        return f"Level(id={self.id!r}, Theme={self.theme!r}, Difficult={self.difficult!r})"

class Questions(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    points = Column(Integer, nullable=False)
    level = Column(Integer, ForeignKey("levels.id"), nullable=False)
    # answer = relationship("Answers", back_populates="question", cascade='all, delete-orphan')
    def __repr__(self):
        return f"Level(id={self.level!r}), Question(id={self.id!r}, Description={self.description!r})"

class Answers(Base):
    __tablename__ = "answers"
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    question = Column(Integer, ForeignKey("questions.id"), nullable=False)
    def __repr__(self):
        return f"Question(id={self.question!r}, Description={self.description!r})"