from App.gateway.database.database_models import Answers, Questions
from App.domain.models.answer_model import AnswerDTO

class AnswerRepository:
    def __init__(self, conn):
        self.conn = conn

    def create(self, answer):
        try:
            db_answer = Answers()
            db_answer.description = answer['description']
            db_answer.question = answer['question']

            self.conn.add(db_answer)
            self.conn.flush()
            self.conn.refresh(db_answer)
            self.conn.commit()

            return AnswerDTO(
                id=db_answer.id,
                description=db_answer.description,
                question=db_answer.question
            )
        except Exception as ex:
            raise ex
        finally:
            self.conn.close()

    def detail(self, id):
        try:
            db_answer = self.conn.query(Answers).get(id)

            if db_answer:
                return AnswerDTO(
                    id=db_answer.id,
                    description=db_answer.description,
                    question=db_answer.question
                )
        except Exception as ex:
            raise ex
        finally:
            self.conn.close()  

    def list_by_level(self, level_id):
        try:
            db_answers = self.conn.query(Answers).join(Questions).filter_by(level = level_id).all()
            list_dto = []

            if db_answers:
                for answer in db_answers:
                    list_dto.append(
                        AnswerDTO(
                            id=answer.id,
                            description=answer.description,
                        ))
                return list_dto
        except Exception as ex:
            raise ex
        finally:
            self.conn.close()
