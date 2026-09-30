The main application logic is written in the app module to connect the different components of the system. It handles incoming requests, processes user input, calls the required services or business logic, and returns the appropriate response. This keeps the application organized and makes the core functionality easier to maintain and extend.

Coding — app/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="My Application",
    description="Main application logic",
    version="1.0.0"
)


# -----------------------------
# Request Model
# -----------------------------
class UserRequest(BaseModel):
    name: str
    email: str
    message: str


# -----------------------------
# Home Route
# -----------------------------
@app.get("/")
def home():
    return {
        "message": "Application is running successfully"
    }


# -----------------------------
# Health Check
# -----------------------------
@app.get("/health")
def health():
    return {
        "status": "OK"
    }


# -----------------------------
# Main Application Logic
# -----------------------------
def process_user_input(data: UserRequest):

    if not data.name.strip():
        raise ValueError("Name is required")

    if not data.email.strip():
        raise ValueError("Email is required")

    if not data.message.strip():
        raise ValueError("Message is required")

    # Main processing logic
    result = {
        "name": data.name,
        "email": data.email,
        "message": data.message,
        "processed": True
    }

    return result


# -----------------------------
# User Processing API
# -----------------------------
@app.post("/process")
def process_request(data: UserRequest):

    try:
        result = process_user_input(data)

        return {
            "success": True,
            "data": result
        }

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )


# -----------------------------
# Application Status
# -----------------------------
@app.get("/status")
def application_status():

    return {
        "application": "My Application",
        "status": "running",
        "version": "1.0.0"
    }
Project Structure
project/
│
├── app/
│   ├── __init__.py
│   └── main.py
│
├── requirements.txt
└── README.md
requirements.txt
fastapi
uvicorn
pydantic
Run the Application
pip install -r requirements.txt
uvicorn app.main:app --reload

Open:

http://127.0.0.1:8000

For API testing:

http://127.0.0.1:8000/docs
