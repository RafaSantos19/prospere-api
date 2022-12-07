from flask import Blueprint, Flask
from flask_cors import CORS
from App.api import api
from App.controller.authentication.authentication_controller import AuthenticationController
from App.controller.user.create_user_controller import CreateUserController
from App.controller.user.details_user_controller import DetailsUserController
from App.controller.user.update_user_controller import UpdateUserController
from App.controller.user.update_user_xp_controller import UpdateUserXPController
from App.controller.levels.details_level_controller import DetailsLevelController
from App.controller.levels.list_levels_controller import ListLevelsController
from App.controller.questions.details_questions_controller import DetailsQuestionsController
from App.controller.answer.list_answer_controller import ListAnswerController
from App.controller.create_challenges_controller import CreateChallengesController
from App.controller.answer.check_answer_controller import CheckAnswerController

def initialize(app):
    blueprint = Blueprint('api', __name__)

    api.init_app(blueprint)

    api.add_resource(CreateChallengesController, "/challenges")
    api.add_resource(AuthenticationController, "/auth/login") 
    api.add_resource(CreateUserController, "/auth/signup")
    api.add_resource(DetailsUserController, "/user/<string:id>")
    api.add_resource(UpdateUserController, "/user/<string:id>")
    api.add_resource(UpdateUserXPController, "/user/<string:id>/xp/<string:xp>")
    api.add_resource(DetailsLevelController, "/level/<string:id>")
    api.add_resource(ListLevelsController, "/level/list")
    # api.add_resource(ListQuestionsController, "/level/<string:id>/questions")
    api.add_resource(DetailsQuestionsController, "/question/<string:id>")
    api.add_resource(ListAnswerController, "/question/<string:id>/answers/list")
    api.add_resource(CheckAnswerController, "/question/<string:id>/answer/<string:answer_id>")

    app.register_blueprint(blueprint)
    CORS(app)
    return app

app = initialize(Flask(__name__))