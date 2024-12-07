from fastapi import FastAPI
from pydantic import BaseModel
import httpx

app = FastAPI()

# Pydantic model for User
class User(BaseModel):
    username: str
    email: str
    password: str

users_db = {}
notification_service_url = "http://notification-service:8002/notifications/"

@app.get("/")
def read_root():
    return {"message": "Welcome to the User Service!"}
@app.post("/users/")
async def create_user(user: User):
    if user.username in users_db:
        return {"message": "Username already exists"}
    
    users_db[user.username] = user

    # Notify about the new user creation
    async with httpx.AsyncClient() as client:
        response = await client.post(notification_service_url, json={"message": f"New user created: {user.username}"})

    return {"message": "User created", "user": user}

@app.get("/users/{username}")
def get_user(username: str):
    user = users_db.get(username)
    if user is None:
        return {"message": "User not found"}
    return {"username": username, "user": user}
