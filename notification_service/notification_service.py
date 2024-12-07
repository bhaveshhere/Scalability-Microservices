from fastapi import FastAPI
from typing import List


app = FastAPI()

notifications_db = []

@app.post("/notifications/")
def create_notification(message: str):
    notifications_db.append(message)
    return {"message": "Notification created", "notification": message}

@app.get("/notifications/")
def get_notifications() -> List[str]:
    return notifications_db