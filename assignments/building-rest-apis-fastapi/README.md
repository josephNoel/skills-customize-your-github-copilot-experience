# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI to practice routes, HTTP methods, request data, and path and query parameters.

## 📝 Tasks

### 🛠️ Create the API and a Read Route

#### Description
Set up a FastAPI application and create endpoints that return task information.

#### Requirements
Completed program should:

- Create a FastAPI app in `main.py`
- Add a `GET /` endpoint that returns a welcome message
- Add a `GET /tasks` endpoint that returns the in-memory task list
- Run locally with `uvicorn main:app --reload`


### 🛠️ Add and Retrieve Tasks

#### Description
Use a Pydantic model and dynamic routes to create and retrieve tasks.

#### Requirements
Completed program should:

- Define a `Task` model with an integer `id`, string `title`, and boolean `completed`
- Add a `POST /tasks` endpoint that accepts a `Task` and adds it to the task list
- Add a `GET /tasks/{task_id}` endpoint that retrieves a task by ID
- Return an appropriate error response when a requested task is not found


### 🛠️ Filter Tasks

#### Description
Add a query parameter that allows clients to filter the returned tasks.

#### Requirements
Completed program should:

- Update `GET /tasks` to accept an optional `completed` query parameter
- Return only completed tasks when `completed=true`
- Return only incomplete tasks when `completed=false`
- Return all tasks when `completed` is omitted
