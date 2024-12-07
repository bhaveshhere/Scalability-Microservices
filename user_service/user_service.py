from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Pydantic model for User
class User(BaseModel):
    username: str
    email: str
    password: str

users_db = {}

@app.post("/users/")
def create_user(user: User):
    if user.username in users_db:
        return {"message": "Username already exists"}
    users_db[user.username] = user
    return {"message": "User created", "user": user}

@app.get("/users/{username}")
def get_user(username: str):
    user = users_db.get(username)
    if user is None:
        return {"message": "User not found"}
    return {"username": username, "user": user}