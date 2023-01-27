from pydantic import BaseModel


class AuthRegisterDto(BaseModel):
    username: str
    password: str


class AuthLoginDto(BaseModel):
    username: str
    password: str
