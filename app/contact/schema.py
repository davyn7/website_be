from typing import Optional
from sqlmodel import Field, SQLModel
# from pydantic import EmailStr
import datetime

# Create an email model
class ContactTemp(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    subject: str
    email_address: str
    message: str

class Contact(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    subject: str
    email_address: str
    message: str
    date: datetime.datetime = Field(default=datetime.datetime.utcnow)