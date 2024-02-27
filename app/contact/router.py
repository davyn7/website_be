from fastapi import FastAPI, APIRouter, Request, HTTPException
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from app.contact.schema import Contact, ContactTemp
from app.db import engine
from sqlmodel import Session, create_engine, select
from sqlalchemy.orm import load_only
from dotenv import load_dotenv
import os
import datetime
from email_validator import validate_email, EmailNotValidError
import asyncio

load_dotenv()

router = APIRouter(
    prefix="/contact",
    tags=["contact"],
)


# conf = ConnectionConfig(
#     MAIL_USERNAME = os.getenv("CONTACT_EMAIL_FROM"),
#     MAIL_PASSWORD = os.getenv("CONTACT_EMAIL_PASSWORD"),
#     MAIL_FROM = os.getenv("CONTACT_EMAIL_FROM"),
#     MAIL_PORT = 587,
#     MAIL_SERVER = "smtp.gmail.com",
#     MAIL_FROM_NAME = "davyn.io Contact Form",
#     MAIL_STARTTLS = True,
#     MAIL_SSL_TLS = False,
#     USE_CREDENTIALS = True,
#     VALIDATE_CERTS = True
# )

# Get all messages
@router.get("/all")
async def getAllMessages():
    with Session(engine) as session:
        messages = session.exec(select(Contact)).all()
        return messages, {"result": "Messages Retrieved"}

# Get a message by id
@router.get("/details")
async def getMessage(id: int):
    with Session(engine) as session:
        message = session.exec(select(Contact).where(Contact.id == id)).first()
        if not message:
            raise HTTPException(status_code=404, detail="Message not found")
        return message, {"result": "Message Retrieved"}

# Send a message
@router.post("/send-message")
async def sendMessage(contact: ContactTemp):
    # try:
    #     v = validate_email(contact.email_address)
    #     email = v["email"]
    # except EmailNotValidError as e:
    #     raise HTTPException(status_code=400, detail=str(e))
    # message = MessageSchema(
    #     subject=contact.subject,
    #     recipients=[os.getenv("CONTACT_EMAIL_TO")],
    #     body=f"Name: {contact.name}\nEmail: {contact.email_address}\nMessage: {contact.message}",
    #     subtype=MessageType.plain
    # )
    # fm = FastMail(conf)
    # await fm.send_message(message)
    with Session(engine) as session:
        session.add(Contact(name=contact.name, subject=contact.subject, email_address=contact.email_address, message=contact.message, date=datetime.datetime.utcnow()))
        session.commit()
        return {"message": "Message Sent"}

# Delete a message
@router.delete("/delete")
async def deleteMessage(id: int):
    with Session(engine) as session:
        contact = session.exec(select(Contact).where(Contact.id == id)).first()
        if not contact:
            raise HTTPException(status_code=404, detail="Message not found")
        session.delete(contact)
        session.commit()
        return {"result": "Message Deleted"}