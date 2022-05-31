from fastapi import APIRouter
from router import signup

router = APIRouter()
router.include_router(signup.app, tags=["sign_up"], prefix="/signup")
