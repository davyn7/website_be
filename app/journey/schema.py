from typing import Optional
from sqlmodel import Field, SQLModel
import datetime

# Create a journey model
class Journey(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    short_description: str
    long_description: str
    year: int
    month: Optional[int]
    day: Optional[int]

# Create a journey model
class JourneyUpdate(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: Optional[str]
    short_description: Optional[str]
    long_description: Optional[str]
    year: Optional[int]
    month: Optional[int]
    day: Optional[int]