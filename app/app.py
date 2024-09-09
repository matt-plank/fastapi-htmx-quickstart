from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.responses import component

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def index():
    return component(
        "pages/index.html",
        "index_page",
        {},
    )
