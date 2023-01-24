from flask import Blueprint

import controllers.auth

blueprint = Blueprint("api", __name__)
blueprint.register_blueprint(controllers.auth.blueprint)