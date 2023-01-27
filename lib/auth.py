# authorization and authentication subsystem

from dataclasses import dataclass
from typing import Optional

import jwt
from fastapi import Header, HTTPException

import controllers.auth
from models.user import UserRole


@dataclass
class UserMetadata:
    userId: int
    role: int


class AuthDependency:
    accepted_roles: [int]

    def __init__(self, accepted_roles=[UserRole.USER]):
        self.accepted_roles = accepted_roles

    def __call__(self, authorization: Optional[str] = Header(default=None)) -> UserMetadata:
        if not authorization:
            raise HTTPException(401, "unauthorized")

        try:
            data = jwt.decode(authorization.split()[1], controllers.auth.jwt_key, algorithms=["HS256"])
        except jwt.exceptions.ExpiredSignatureError:
            raise HTTPException(401, "tokenExpired")
        except jwt.exceptions.InvalidTokenError as e:
            raise HTTPException(401, "invalidToken")
        except Exception:
            raise HTTPException(401, "unknownError")

        if not (data.get("role") in self.accepted_roles):
            raise HTTPException(403, "permissionDenied")

        return UserMetadata(data.get("userId"), data.get("role"))
