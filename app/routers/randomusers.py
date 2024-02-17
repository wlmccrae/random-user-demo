from fastapi import APIRouter, Depends
import requests

from models.users import UserIn, UserOut, UserOut, UsersOut
from queries.users import UserQueries

router = APIRouter()

@router.post("/app/randomuser", response_model=UserOut)
async def generate_user(
    queries: UserQueries = Depends(),
):
    url = "https://randomuser.me/api/"
    info = {}

    # Make the API call to fetch a random user.
    try:
        response = requests.get(url)
        raw_user = response.json()
        random_user = raw_user["results"][0]
        # print(f"*******Random User Fetched: {random_user}")

        info["name"] = random_user["name"]["first"] + ' ' + random_user["name"]["last"]
        info["dob"] = random_user["dob"]["date"]
        info["email"] = random_user["email"]
        info["city"] = random_user["location"]["city"]
        info["state"] = random_user["location"]["state"]
        info["country"] = random_user["location"]["country"]
        # print(f"*******User to write to database: {info}")

    except requests.exceptions.RequestException as e:
        print(f"*******There was an error: {e}.")
        return None

    # Turn the Python dictionary into a Pydantic model.
    pyinfo = UserIn(**info)
    return queries.create_user(pyinfo)

@router.get("/app/randomusers", response_model=UsersOut)
def get_users(
    queries: UserQueries = Depends(),
):
    return {"users": queries.get_users()}
