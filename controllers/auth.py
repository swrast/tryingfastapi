from flask import request, Blueprint

blueprint = Blueprint("auth", __name__)


@blueprint.route("/api/auth/register", methods=["POST"])
async def register():
    print(request)

    return "ok"
