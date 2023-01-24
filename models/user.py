from peewee import CharField, BlobField
from database import BaseModel


class User(BaseModel):
    username = CharField(unique=True)
    password = BlobField()
