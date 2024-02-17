from fastapi import APIRouter
import requests

from models.users import UserIn, UserOut, UsersOut

router = APIRouter()

@router.get("/randomuser")
def generate_users():
    url = "https://randomuser.me/api/"
    try:
        response = requests.get(url)
        random_user = response.json()
        print(f"*******Random User Fetched: {random_user}")
        return random_user
    except requests.exceptions.RequestException as e:
        print(f"*******There was an error: {e}.")
        return None

# @router.get("/randomusers/{user_id}")
# def get_user(user_id: int):
#     return users[user_id]

# @router.put("/randomusers/")
# def create_user()
