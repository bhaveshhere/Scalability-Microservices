from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
 
app = FastAPI()
 
follows_db = {}
 
class FollowRequest(BaseModel):
    follower: str
    following: str
 
@app.post("/follow/")
def follow_user(request: FollowRequest):
    follower = request.follower
    following = request.following
    if follower not in follows_db:
        follows_db[follower] = []
    if following not in follows_db[follower]:
        follows_db[follower].append(following)
    return {"message": f"{follower} is now following {following}"}
 
@app.get("/followers/{username}")
def get_followers(username: str) -> dict:
    followers = [follower for follower, following in follows_db.items() if username in following]
    return {"followers": followers}
 
@app.get("/following/{username}")
def get_following(username: str) -> dict:
    following = follows_db.get(username, [])
    return {"following": following}
