from fastapi import FastAPI

from app.responses import component

app = FastAPI()


@app.get("/")
async def index():
    return component(
        "pages/index.html",
        "index_page",
        {},
    )
