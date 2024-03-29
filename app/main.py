from fastapi import FastAPI

from routers import users

description = """
A FastAPI backend that fetches randomly generated users from the Random User Generator API and saves them to a PostgreSQL database.

You will be able to:
* **Create** a random user and write their info to the database.
* **Retrieve** the list of all users.
* **Retrieve** a user's info.
* **Update** a user's info.
* **Delete** a user.
"""

app = FastAPI(
    title="Random User Generator Demo",
    description=description,
    version="1.0",
    contact={
        "name": "Wanda McCrae",
        "url": "https://wlmccrae.wordpress.com"
    },
)
app.include_router(users.router, tags=["USERS"])
