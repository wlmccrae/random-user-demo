# Random User Generator Demo

## Creator
- Name: Wanda McCrae
- Date: February 2024

A FastAPI backend that fetches randomly generated users from the [Random User Generator API](https://randomuser.me/) and saves them to a PostgreSQL database.

## Project Initialization

How to use this application locally using Docker:

1. Clone this repository to your local machine.
2. CD into the new directory.
3. Run **docker volume create fastapidemo-data**.
4. Run **docker-compose build --no-cache**.
5. Run **docker-compose up**.

If you are using Docker Desktop, you can interact with the containers in that application. To interact with the FastAPI container from the terminal:

6. Run **docker exec -it random-user-demo-fastapi-1 bash**.

## Design
After the application is running locally, you can interact with the application's documentation [in your web browser](http://localhost:8000/docs).
