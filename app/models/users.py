from pydantic import BaseModel


class UserIn(BaseModel):
    first_name: str
    last_name: str
    gender: str
    email: str


class UserOut(BaseModel):
    id: int
    first_name: str
    last_name: str
    gender: str
    email: str


class UsersOut(BaseModel):
    users: list[UserOut]
