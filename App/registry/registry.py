from App.domain.services.answer_service import AnswerService
from App.domain.services.level_service import LevelService
from App.domain.services.question_service import QuestionsService
from App.domain.services.authentication_service import AuthenticationService
from App.domain.services.user_service import UserService
from App.gateway.security.jwt import JWT
from App.gateway.database.conn import Database
from App.gateway.repository.answer_repository import AnswerRepository
from App.gateway.repository.level_repository import LevelRepository
from App.gateway.repository.questions_repository import QuestionRepository
from App.gateway.repository.user_repository import UserRepository
from App.usecase.authentication_usecase import AuthenticationUsecase
from App.usecase.create_challenges_usecase import CreateChallengeUsecase
from App.usecase.user.create_user_usecase import CreateUserUsecase
from App.usecase.user.details_user_usecase import DetailsUserUsecase
from App.usecase.user.update_user_usecase import UpdateUserUsecase
from App.usecase.user.update_user_xp_usecase import UpdateUserXPUsecase
from App.usecase.levels.details_level_usecase import DetailsLevelUsecase
from App.usecase.questions.details_questions_usecase import DetailsQuestionsUsecase
from App.usecase.answer.list_answer_usecase import ListAnswerUsecase
from App.usecase.answer.check_answer_usecase import CheckAnswerUsecase
from App.usecase.levels.list_levels_usecase import ListLevelsUsecase
from config import Config

class Registry:
    def __init__(self):
        self.config = Config
        self.repository_session = Database().session_factory()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Registry, cls).__new__(cls)
        return cls.instance


    def create_challenges_usecase(self):
        return CreateChallengeUsecase(
            LevelService(LevelRepository(self.repository_session)),
            QuestionsService(QuestionRepository(self.repository_session)),
            AnswerService(AnswerRepository(self.repository_session))
        )

    def authentication_usecase(self):
        return AuthenticationUsecase(
            AuthenticationService(JWT(self.config)),
            UserService(
                UserRepository(
                    self.repository_session
                )
            )
        )

    def create_user_usecase(self):
        return CreateUserUsecase(
            AuthenticationService(JWT(self.config)),
            UserService(UserRepository(self.repository_session))
        )

    def update_user_usecase(self):
        return UpdateUserUsecase(
            UserService(UserRepository(self.repository_session)),
            AuthenticationService(JWT(self.config))
        )

    def update_user_xp_usecase(self):
        return UpdateUserXPUsecase(
            UserService(UserRepository(self.repository_session))
        )

    def details_user_usecase(self):
        return DetailsUserUsecase(
            UserService(UserRepository(self.repository_session))
        )

    def details_level_usecase(self):
        return DetailsLevelUsecase(
            LevelService(LevelRepository(self.repository_session)),
            QuestionsService(QuestionRepository(self.repository_session))

        )
      
    def list_levels_usecase(self):
        return ListLevelsUsecase(
            LevelService(LevelRepository(self.repository_session)),
    )
      
    def details_questions_usecase(self):
        return DetailsQuestionsUsecase(
            QuestionsService(QuestionRepository(self.repository_session))
        )

    def list_answer_usecase(self):
        return ListAnswerUsecase(
            AnswerService(AnswerRepository(self.repository_session)),
            QuestionsService(QuestionRepository(self.repository_session))
        )

    def check_answer_usecase(self):
        return CheckAnswerUsecase(
            AnswerService(AnswerRepository(self.repository_session))
        )            