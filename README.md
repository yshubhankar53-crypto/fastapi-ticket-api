# FastAPI Ticket API

A simple REST API for creating support tickets using FastAPI and Pydantic validation.


## Features


- POST endpoint for ticket creation

- Request validation using Pydantic

- Email format validation

- Structured JSON responses

## Example Request

POST /tickets

{
  "title": "Login issue",
  "description": "Unable to login with valid credentials",
  "email": "user@example.com"
}

## How to Run

pip install -r requirements.txt
uvicorn app.main:app --reload

