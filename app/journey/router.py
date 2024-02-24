# Router
# CRUD object

from fastapi import FastAPI, APIRouter
import asyncio

router = APIRouter(
    prefix="/journey",
    tags=["journey"],
)

@router.get("/health_check")
async def health_check():
    return {"result": "ok"}