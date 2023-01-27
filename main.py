import asyncio
import os

from dotenv import load_dotenv
from fastapi import FastAPI
from hypercorn.config import Config
from hypercorn.asyncio import serve
from tortoise import Tortoise

if __name__ == "__main__":
    load_dotenv()

import controllers

app = FastAPI()
app.include_router(controllers.router)


async def main():
    await Tortoise.init(
        db_url=os.getenv("SERVER_DB_URI"),
        modules={"models": ["models"]}
    )
    await Tortoise.generate_schemas()

    await serve(app, Config())

if __name__ == "__main__":
    asyncio.run(main())
