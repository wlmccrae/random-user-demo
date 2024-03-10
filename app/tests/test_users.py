from fastapi.testclient import TestClient
from queries.users import UserQueries
from main import app

client = TestClient(app)


class FakeUserQueries:
    def create_user(self, user_info):
        # The route expects data to be passed into the real query,
        # so we need to include that parameter in the fake query
        # even though it isn't actually defined or used.
        return {
            "id": 13,
            "name": "Miro Peltola",
            "dob": "1947-11-22T00:52:50.790Z",
            "email": "miro.peltola@example.com",
            "city": "Tervo",
            "state": "Southern Savonia",
            "country": "Finland"
        }

    def get_user(self, user_id):
        return {
            "id": user_id,
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

    def update_user(self, user_id):
        return {
            "id": user_id,
            "name": "Miro Peltola",
            "dob": "1947-11-22T00:52:50.790Z",
            "email": "miro.peltola@example.com",
            "city": "Tervo",
            "state": "Southern Savonia",
            "country": "Finland"
        }

    def delete_user(self, user_id):
        return True


def test_create_user():
    # Arrange
    app.dependency_overrides[UserQueries] = FakeUserQueries

    # Act
    res = client.post('/app/users')
    data = res.json()

    # Assert
    assert res.status_code == 200
    assert "id" in data
    assert "name" in data
    assert "dob" in data
    assert "email" in data
    assert "city" in data
    assert "state" in data
    assert "country" in data

    # Cleanup
    app.dependency_overrides = {}


def test_get_user():
    # Arrange
    app.dependency_overrides[UserQueries] = FakeUserQueries

    # Act
    res = client.get('/app/users/55')
    data = res.json()

    # Assert
    assert res.status_code == 200
    assert data["id"] == 55
    assert "name" in data
    assert "dob" in data
    assert "email" in data
    assert "city" in data
    assert "state" in data
    assert "country" in data

    # Cleanup
    app.dependency_overrides = {}


def test_get_users():
    # Arrange
    app.dependency_overrides[UserQueries] = FakeUserQueries

    # Act
    res = client.get('/app/users')
    data = res.json()

    # Assert
    assert res.status_code == 200
    assert 'users' in data
    assert len(data["users"]) == 3

    # Cleanup
    app.dependency_overrides = {}


def test_update_user():
    # Arrange
    app.dependency_overrides[UserQueries] = FakeUserQueries
    input_data = {
        "name": "Wanda Lotus"
    }

    # Act
    res = client.get('/app/users/42')
    data = res.json()

    # Assert
    assert res.status_code == 200
    assert data["id"] == 42
    assert "name" in data
    assert "dob" in data
    assert "email" in data
    assert "city" in data
    assert "state" in data
    assert "country" in data
    assert "name" != input_data["name"]

    # Cleanup
    app.dependency_overrides = {}


def test_delete_user():
    # Arrange
    app.dependency_overrides[UserQueries] = FakeUserQueries

    # Act
    res = client.delete('/app/users/12')
    data = res.json()

    # Assert
    assert res.status_code == 200
    assert data is True

    # Cleanup
    app.dependency_overrides = {}
