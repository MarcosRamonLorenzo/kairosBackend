from fastapi import APIRouter
from users.endpoints import router as users_router


# Router principal
router = APIRouter()

router.include_router(users_router, prefix="/users", tags=["users"])

