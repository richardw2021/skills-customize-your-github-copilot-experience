# 📘 Assignment: REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API using the FastAPI framework. In this assignment, students will practice creating routes, handling JSON data, and returning clear API responses.

## 📝 Tasks

### 🛠️ Create API Endpoints

#### Description
Set up a FastAPI application with several endpoints that allow a user to view and add items through HTTP requests.

#### Requirements
Completed program should:

- Create a FastAPI app instance.
- Add a `GET /` route that returns a welcome message.
- Add a `GET /items` route that returns a list of items.
- Add a `POST /items` route that accepts JSON data and adds a new item.
- Return responses in JSON format.

### 🛠️ Validate and Organize the API

#### Description
Improve the API by using a data model for request validation and by keeping the code easy to read and test.

#### Requirements
Completed program should:

- Use a Pydantic model to define the structure of an item.
- Reject invalid request data automatically through FastAPI validation.
- Keep item data in a Python list for this assignment.
- Include clear field names such as `id`, `name`, and `price`.
- Run successfully with `uvicorn` so the endpoints can be tested in a browser or API client.