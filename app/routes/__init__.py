from fastapi import APIRouter
from app.routes.user_routes import router as user_router
from app.routes.post_routes import router as post_router

router = APIRouter()
router.include_router(user_router)
router.include_router(post_router)
