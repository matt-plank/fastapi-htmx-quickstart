from fastapi import APIRouter

from app.responses import component

router = APIRouter()


@router.get("/")
async def index_page():
    return component(
        "pages/index.html",
        "index_page",
        {},
    )
