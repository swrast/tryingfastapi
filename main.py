from dotenv import load_dotenv
from flask import Flask

if __name__ == "__main__":
    load_dotenv()

from database import db
from controllers import blueprint

import models

app = Flask(__name__)

app.register_blueprint(blueprint)

if __name__ == "__main__":
    print(" * Setting database up")

    db.connect()
    db.create_tables(models.models)

    app.run()
