from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_root_returns_welcome_message():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Task API"}


# TODO: Add tests for listing, creating, and retrieving tasks.
# TODO: Add tests for unknown task IDs and invalid request data.
