from fastapi import FastAPI

from routers import users

description = """
A FastAPI backend that fetches randomly generated users from the Random User Generator API and saves them to a PostgreSQL database.
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
