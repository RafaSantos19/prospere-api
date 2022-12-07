from App.gateway.database.database_models import Questions
from App.domain.models.questions_model import QuestionDTO
from App.gateway.database.database_models import Levels

class QuestionRepository:
    def __init__(self, conn):
        self.conn = conn

    def create(self, question):
        try:
            db_question = Questions()
            db_question.description = question['description']
            db_question.points = question['points']
            db_question.level = question['level']

            self.conn.add(db_question)
            self.conn.flush()
            self.conn.refresh(db_question)
            self.conn.commit()

            return QuestionDTO(
                id=db_question.id,
                points=db_question.points,
                description=db_question.description,
            )
        except Exception as ex:
            raise ex
        finally:
            self.conn.close()

    def detail(self, id):
        try:
            db_question = self.conn.query(Questions).get(id)

            if db_question:
                return QuestionDTO(
                    id=db_question.id,
                    points=db_question.points,
                    description=db_question.description,
                    level=db_question.level,
                )
        except Exception as ex:
            raise ex
        finally:
            self.conn.close()  

    def list(self, level_id):
        try:
            db_questions = self.conn.query(Questions).filter_by(level = level_id).all()
            list_dto = []

            if db_questions:
                for level in db_questions:
                    list_dto.append(
                        QuestionDTO(
                            id=level.id,
                            points=level.points,
                            # description=level.description,
                        ))
                return list_dto
        except Exception as ex:
            raise ex
        finally:
            self.conn.close()
