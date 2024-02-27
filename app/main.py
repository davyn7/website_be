from typing import Union

from fastapi import FastAPI
from app.journey.router import router as journey_router
from app.media.router import router as media_router
from app.booking.router import router as booking_router
from app.donation.router import router as donation_router
from app.investor.router import router as investor_router
from app.user.router import router as user_router
from app.contact.router import router as contact_router
from app.content.router import router as content_router
from app.db import create_db_and_tables

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

app.include_router(journey_router)
app.include_router(media_router)
app.include_router(booking_router)
app.include_router(donation_router)
app.include_router(investor_router)
app.include_router(user_router)
app.include_router(contact_router)
app.include_router(content_router)