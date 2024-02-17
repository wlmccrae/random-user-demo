from pydantic import BaseModel


class UserIn(BaseModel):
    name: str
    dob: str
    email: str
    city: str
    state: str
    country: str


class UserOut(BaseModel):
    id: int
    name: str
    dob: str
    email: str
    city: str
    state: str
    country: str


class UsersOut(BaseModel):
    users: list[UserOut]
