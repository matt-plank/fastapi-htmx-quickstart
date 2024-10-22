from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app import config, database
from app.routes import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    database.init(config.database_url())
    yield


app = FastAPI(lifespan=lifespan)
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
app.include_router(router)
