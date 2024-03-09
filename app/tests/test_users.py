from fastapi.testclient import TestClient
from queries.users import UserQueries
from main import app

client = TestClient(app)


class FakeUserQueries:
    def create_user(self):
        return {
            "id": 13,
            "name": "Miro Peltola",
            "dob": "1947-11-22T00:52:50.790Z",
            "email": "miro.peltola@example.com",
            "city": "Tervo",
            "state": "Southern Savonia",
            "country": "Finland"
        }

    def get_users(self):
        return [
            {
                "id": 1,
                "name": "Miriam Niemeyer",
                "dob": "1973-11-08T16:56:03.590Z",
                "email": "miriam.niemeyer@example.com",
                "city": "Triberg im Schwarzwald",
                "state": "Berlin",
                "country": "Germany"
            },
            {
                "id": 2,
                "name": "Antonio Gómez",
                "dob": "1946-06-22T00:24:53.882Z",
                "email": "antonio.gomez@example.com",
                "city": "Ferrol",
                "state": "Islas Baleares",
                "country": "Spain"
            },
            {
                "id": 3,
                "name": "Sheila Morris",
                "dob": "1967-04-13T21:11:03.762Z",
                "email": "sheila.morris@example.com",
                "city": "Albany",
                "state": "Tasmania",
                "country": "Australia"
            }
        ]


# def test_create_user():
#     # Arrange
#     app.dependency_overrides[UserQueries] = FakeUserQueries

#     # Act
#     res = client.post('/app/users')

#     # Assert
#     assert res.status_code == 200

#     # Cleanup


def test_get_users():
    # Arrange
    app.dependency_overrides[UserQueries] = FakeUserQueries

    # Act
    res = client.get('/app/users')

    # Assert
    assert res.status_code == 200

    # Cleanup
