from fastapi import APIRouter, Depends, Response
import requests

from models.users import UserIn, UserOut, UserOut, UsersOut
from queries.users import UserQueries

router = APIRouter()

@router.post("/app/user", response_model=UserOut)
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

        info["name"] = random_user["name"]["first"] + ' ' + random_user["name"]["last"]
        info["dob"] = random_user["dob"]["date"]
        info["email"] = random_user["email"]
        info["city"] = random_user["location"]["city"]
        info["state"] = random_user["location"]["state"]
        info["country"] = random_user["location"]["country"]

    except requests.exceptions.RequestException as e:
        print(f"*******There was an error: {e}.")
        return None

    # Turn the Python dictionary into a Pydantic model.
    pyinfo = UserIn(**info)
    return queries.create_user(pyinfo)

@router.get("/app/users", response_model=UsersOut)
def get_users(
    queries: UserQueries = Depends(),
):
    return {"users": queries.get_users()}

@router.get("/app/user/{user_id}", response_model=UserOut)
def get_user(
    user_id: int,
    response: Response,
    queries: UserQueries = Depends(),
):
    record = queries.get_user(user_id)
    if record is None:
        response.status_code = 404
    else:
        return record
