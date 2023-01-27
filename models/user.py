from tortoise import Model
from tortoise import fields


class UserRole:
    USER = 1
    ADMIN = 2


class User(Model):
    id = fields.IntField(pk=True)

    username = fields.TextField()
    password = fields.CharField(max_length=97)
    role = fields.IntField()
