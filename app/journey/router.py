from fastapi import FastAPI, APIRouter, Request, HTTPException
from app.journey.schema import Journey, JourneyUpdate
from app.db import engine
from sqlmodel import Session, create_engine, select
from sqlalchemy.orm import load_only
import asyncio

router = APIRouter(
    prefix="/journey",
    tags=["journey"],
)

@router.get("/health_check")
async def health_check():
    return {"result": "ok"}

# Get journey highlights
@router.get("/highlights")
async def getJourneyHighlights():
    with Session(engine) as session:
        # journeys = session.exec(select(Journey).options(load_only("name", "short_description"))).all()
        journeys = session.exec(select(Journey)).all()
        journeys = [{"name": journey.name, "short_description": journey.short_description} for journey in journeys]
        return journeys, {"result": "Journey Highlights Retrieved"}

# Get all journeys
@router.get("/all")
async def getAllJourneys():
    with Session(engine) as session:
        journeys = session.exec(select(Journey)).all()
        return journeys, {"result": "Journeys Retrieved"}

# Get one journey details
@router.post("/details")
async def getJourneyDetails(id: int):
    with Session(engine) as session:
        journey = session.exec(select(Journey).where(Journey.id == id)).first()
        if not journey:
            raise HTTPException(status_code=404, detail="Journey not found")
        return journey, {"result": "Journey Details Retrieved"}

# Add a new journey
@router.post("/add")
async def addJourney(journey: Journey):
    with Session(engine) as session:
        session.add(journey)
        session.commit()
        return {"result": "Journey Added"}
    
# Update a journey
@router.post("/update")
async def updateJourney(id: int, update: JourneyUpdate):
    with Session(engine) as session:
        journey = session.exec(select(Journey).where(Journey.id == id)).first()
        if not journey:
            raise HTTPException(status_code=404, detail="Journey not found")
        for key, value in update.dict().items():
            if value is not None and key is not "id":
                setattr(journey, key, value)
        session.add(journey)
        session.commit()
        return {"result": "Journey Updated"}

# Delete a journey
@router.post("/delete")
async def deleteJourney(id: int):
    with Session(engine) as session:
        journey = session.exec(select(Journey).where(Journey.id == id)).first()
        if not journey:
            raise HTTPException(status_code=404, detail="Journey not found")
        session.delete(journey)
        session.commit()
        return {"result": "Journey Deleted"}