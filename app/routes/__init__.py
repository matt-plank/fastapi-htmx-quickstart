from fastapi import APIRouter

from app.routes.healthcheck import router as healthcheck_router
from app.routes.index import router as index_router

router = APIRouter()
router.include_router(healthcheck_router)
router.include_router(index_router)
