import asyncio
import os

from dotenv import load_dotenv
from flask import Flask, make_response, jsonify
from jsonschema.exceptions import ValidationError
from tortoise import Tortoise

if __name__ == "__main__":
    load_dotenv()

from controllers import blueprint

app = Flask(__name__)


@app.errorhandler(400)
def bad_request(error):
    if isinstance(error.description, ValidationError):
        original_error = error.description
        return make_response(jsonify({'error': "invalidData", "description": original_error.message,
                                      "properties": original_error.schema["properties"]}), 400)

    return error


app.register_blueprint(blueprint)


async def main():
    print(" * Setting database up")

    await Tortoise.init(
        db_url=os.getenv("SERVER_DB_URI"),
        modules={"models": ["dbmodels"]}
    )
    await Tortoise.generate_schemas()

    app.run()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
