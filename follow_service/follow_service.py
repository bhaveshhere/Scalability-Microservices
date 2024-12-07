from fastapi import FastAPI
from typing import List

app = FastAPI()

follows_db = {}

@app.post("/follow/")
def follow_user(follower: str, following: str):
    if follower not in follows_db:
        follows_db[follower] = []
    if following not in follows_db[follower]:
        follows_db[follower].append(following)
    return {"message": f"{follower} is now following {following}"}

@app.get("/followers/{username}")
def get_followers(username: str) -> List[str]:
    followers = [follower for follower, following in follows_db.items() if username in following]
    return {"followers": followers}

@app.get("/following/{username}")
def get_following(username: str) -> List[str]:
    following = follows_db.get(username, [])
    return {"following": following}
