# Random User Generator Demo

**Author:** Wanda McCrae
**Created:** February 2024

A FastAPI backend that fetches randomly generated users from the [Random User Generator API](https://randomuser.me/) and saves them to a PostgreSQL database.

## Tech Stack

- **FastAPI** — REST API framework
- **PostgreSQL** — database (via psycopg3)
- **Docker / Docker Compose** — containerized local development
- **Pydantic** — data validation and serialization

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/app/users` | Fetch a random user from the external API and save to the database |
| `GET` | `/app/users` | Retrieve all users |
| `GET` | `/app/users/{user_id}` | Retrieve a single user by ID |
| `PUT` | `/app/users/{user_id}` | Update a user's info |
| `DELETE` | `/app/users/{user_id}` | Delete a user |

Each user record stores: name, date of birth, email, city, state, and country.

## Project Structure

```
app/
├── main.py            # FastAPI app setup
├── routers/users.py   # Route handlers
├── models/users.py    # Pydantic models
├── queries/users.py   # Database queries
├── migrations/        # Database migrations
├── tests/             # Tests
└── requirements.txt
docker-compose.yaml
```

## Local Setup (Docker)

1. Clone this repository.
2. `cd` into the project directory.
3. Run `docker volume create fastapidemo-data`
4. Run `docker-compose build --no-cache`
5. Run `docker-compose up`

To open a shell in the FastAPI container:

```bash
docker exec -it random-user-demo-fastapi-1 bash
```

## Interactive Docs

Once running, visit [http://localhost:8000/docs](http://localhost:8000/docs) to explore and test the API via the auto-generated Swagger UI.
