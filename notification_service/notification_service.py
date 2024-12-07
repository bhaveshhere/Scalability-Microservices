from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
 
app = FastAPI()
 
notifications_db = {}
 
class NotificationRequest(BaseModel):
    user: str
    message: str
 
@app.post("/notify/")
def send_notification(request: NotificationRequest):
    user = request.user
    message = request.message
    if user not in notifications_db:
        notifications_db[user] = []
    notifications_db[user].append(message)
    return {"message": f"Notification sent to {user}"}
 
@app.get("/notifications/{user}")
def get_notifications(user: str) -> dict:
    notifications = notifications_db.get(user, [])
    return {"notifications": notifications}
