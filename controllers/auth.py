import datetime
import os

import jwt
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from fastapi import APIRouter, HTTPException

from models.dto.auth import AuthRegisterDto, AuthLoginDto
from models.user import User, UserRole

router = APIRouter(prefix="/auth")

ph = PasswordHasher(hash_len=32)

jwt_key = open(os.getenv("SERVER_SECRET_PATH"), "rb").read()


@router.post("/register")
async def register(data: AuthRegisterDto):
    if await User.get_or_none(username=data.username):
        raise HTTPException(400, "usernameAlreadyTaken")

    await User.create(username=data.username, password=ph.hash(data.password), role=UserRole.USER)


@router.post("/login")
async def login(data: AuthLoginDto):
    u = await User.get_or_none(username=data.username)
    if not u:
        raise HTTPException(400, "userNotFound")

    try:
        ph.verify(u.password, data.password)
    except VerifyMismatchError:
        raise HTTPException(400, "invalidPassword")

    return jwt.encode({
        "exp": datetime.datetime.now()+datetime.timedelta(days=2),
        "userId": u.id,
        "role": u.role
        # role
    }, jwt_key, algorithm="HS256")
