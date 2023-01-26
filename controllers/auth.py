import argon2
from flask import request, Blueprint
from flask_expects_json import expects_json

from dbmodels import User

blueprint = Blueprint("auth", __name__)


@blueprint.route("/api/auth/register", methods=["POST"])
@expects_json({
    "type": "object",
    "properties": {
        "username": {"type": "string"},
        "password": {"type": "string"}
    },
    "required": ["username", "password"]
})
async def register():
    if await User.get_or_none(username=request.json["username"]):
        return "userExists", 400

    await User.create(username=request.json["username"], password=argon2.hash_password(request.json["password"]))

    return "ok"
