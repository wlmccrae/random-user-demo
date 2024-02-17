from fastapi import FastAPI

from routers import randomusers

app = FastAPI()
app.include_router(randomusers.router, tags=["RANDOMUSERS"])

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
