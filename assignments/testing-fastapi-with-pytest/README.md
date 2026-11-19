# 📘 Assignment: Testing FastAPI Endpoints with pytest

## 🎯 Objective

Write automated tests for a FastAPI application using pytest and FastAPI's `TestClient`. Check successful responses as well as common error cases without running a web server.

## 📝 Tasks

### 🛠️ Set Up the Test Client

#### Description
Install the provided dependencies and use `TestClient` to write and run your first test for the sample API.

#### Requirements
Completed program should:

- Install the packages listed in `requirements.txt`
- Create a `TestClient` for the FastAPI app in `main.py`
- Test that `GET /` returns status code `200` and the expected welcome message
- Run the tests with `pytest`


### 🛠️ Test Successful Endpoint Responses

#### Description
Add tests that send requests to the task endpoints and check both the status codes and returned JSON.

#### Requirements
Completed program should:

- Test that `GET /tasks` returns status code `200` and a list of tasks
- Test that `GET /tasks/1` returns the expected task
- Test that `POST /tasks` accepts valid task data and returns the created task


### 🛠️ Test Error Responses

#### Description
Test how the API responds when a requested task does not exist or submitted data is invalid.

#### Requirements
Completed program should:

- Test that requesting an unknown task ID returns status code `404`
- Test that posting a task without a required field returns status code `422`
- Use clear test names and assertions so a failure indicates what behavior needs attention
