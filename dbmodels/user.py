from tortoise.models import Model
from tortoise import fields


class User(Model):
    username = fields.TextField()
    password = fields.BinaryField()
