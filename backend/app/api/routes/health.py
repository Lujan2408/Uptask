from fastapi import APIRouter
from models import Message

router = APIRouter()

@router.get("/health", status_code=200, response_model=Message)
async def health_check():
    return Message(message="Health check OK")