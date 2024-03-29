from fastapi import APIRouter, Depends
import requests

from models.users import UserIn, UserOut, UsersOut
from queries.users import UserQueries

router = APIRouter()


@router.post("/app/users", response_model=UserOut)
async def create_user(queries: UserQueries = Depends()):
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
async def get_users(queries: UserQueries = Depends()):
    return {"users": queries.get_users()}


@router.get("/app/users/{user_id}", response_model=UserOut)
async def get_user(
    user_id: int,
    queries: UserQueries = Depends(),
):
    record = queries.get_user(user_id)
    if record is None:
        info = {}
        info["id"] = 0
        info["name"] = "NO SUCH USER"
        info["dob"] = ""
        info["email"] = ""
        info["city"] = ""
        info["state"] = ""
        info["country"] = ""
        pyinfo = UserOut(**info)
        return pyinfo
    else:
        return record


@router.put("/app/users/{user_id}", response_model=UserOut)
async def update_user(
    user_id: int,
    user_info: UserIn,
    queries: UserQueries = Depends(),
):
    record = queries.update_user(user_id, user_info)
    if record is None:
        info = {}
        info["id"] = 0
        info["name"] = "NO SUCH USER"
        info["dob"] = ""
        info["email"] = ""
        info["city"] = ""
        info["state"] = ""
        info["country"] = ""
        pyinfo = UserOut(**info)
        return pyinfo
    else:
        return record


@router.delete("/app/users/{user_id}", response_model=bool)
async def delete_user(
    user_id: int,
    queries: UserQueries = Depends(),
):
    return queries.delete_user(user_id)
