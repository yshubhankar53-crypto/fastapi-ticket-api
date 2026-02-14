from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI(title="Ticket API")

class TicketCreate(BaseModel):
    title: str
    description: str
    email: EmailStr

@app.post("/tickets")
def create_ticket(ticket: TicketCreate):
    return {
        "message": "Ticket received successfully",
        "data": ticket.dict()
    }
