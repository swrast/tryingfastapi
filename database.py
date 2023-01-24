import os

from peewee import PostgresqlDatabase, Model

db = PostgresqlDatabase(os.getenv("SERVER_DB_NAME"), user=os.getenv("SERVER_DB_USER"),
                        password=os.getenv("SERVER_DB_PASSWORD"), host=os.getenv("SERVER_DB_HOST"),
                        port=int(os.getenv("SERVER_DB_PORT")) if os.getenv("SERVER_DB_PORT") else None)


class BaseModel(Model):
    class Meta:
        database = db
