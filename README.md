# Task Manager API

A simple REST API built with **Python and FastAPI** that allows users to create, view, update, and delete tasks. This project is designed for beginners to learn backend development and API testing using Postman.

## Features

- Create a new task
- View all tasks
- View a single task by ID
- Update task details
- Delete a task
- Validate task data
- Handle errors for tasks that do not exist
- Test API endpoints using Postman
- Explore API documentation using Swagger UI

## Technologies Used

- **Python** — Programming language
- **FastAPI** — Backend web framework
- **Uvicorn** — ASGI server
- **Pydantic** — Request data validation
- **Postman** — API testing
- **Git and GitHub** — Version control and project hosting

## Project Structure

```text
task-manager-api/
├── .venv/
├── main.py
├── README.md
└── requirements.txt
```

> `.venv/` contains the project's virtual environment and should not normally be uploaded to GitHub.

## Installation and Setup

### 1. Clone the Repository

If the project is on GitHub, run:

```bash
git clone <your-repository-url>
cd task-manager-api
```

Alternatively, open your existing project folder in VS Code or PowerShell.

### 2. Create a Virtual Environment

```powershell
python -m venv .venv
```

### 3. Activate the Virtual Environment

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```powershell
python -m pip install fastapi uvicorn
```

### 5. Create the Requirements File

```powershell
python -m pip freeze > requirements.txt
```

## Run the Application

Start the development server:

```powershell
python -m uvicorn main:app --reload
```

The API will run locally at:

**Base URL:** `http://127.0.0.1:8000`

### API Documentation

Open the following URL in your browser to explore and test the endpoints:

`http://127.0.0.1:8000/docs`

FastAPI automatically generates interactive Swagger documentation.

## API Endpoints

| Method | Endpoint | Description | Expected Status |
|---|---|---|---|
| GET | `/` | Check API status | 200 OK |
| POST | `/tasks` | Create a task | 201 Created |
| GET | `/tasks` | Get all tasks | 200 OK |
| GET | `/tasks/{task_id}` | Get a task by ID | 200 OK |
| PATCH | `/tasks/{task_id}` | Update a task | 200 OK |
| DELETE | `/tasks/{task_id}` | Delete a task | 200 OK |

## Example API Requests

### Create a Task

**Method:** `POST`

**URL:** `http://127.0.0.1:8000/tasks`

**Request Body (JSON):**

```json
{
  "title": "Learn Postman",
  "description": "Test my first backend API",
  "completed": false
}
```

**Example Response:**

```json
{
  "id": 1,
  "title": "Learn Postman",
  "description": "Test my first backend API",
  "completed": false
}
```

### Get All Tasks

**Method:** `GET`

**URL:** `http://127.0.0.1:8000/tasks`

### Update a Task

**Method:** `PATCH`

**URL:** `http://127.0.0.1:8000/tasks/1`

**Request Body:**

```json
{
  "completed": true
}
```

### Delete a Task

**Method:** `DELETE`

**URL:** `http://127.0.0.1:8000/tasks/1`

## API Testing with Postman

You can test the API using Postman by creating requests for each endpoint.

Recommended test cases:

1. Verify that the API is running.
2. Create a task with valid data.
3. Retrieve all tasks.
4. Retrieve a task using its ID.
5. Update a task's completion status.
6. Delete an existing task.
7. Request a nonexistent task and verify that the API returns `404 Not Found`.
8. Submit invalid task data and verify that validation errors are returned.

## Error Handling

The API handles common errors, including:

- **404 Not Found:** The requested task does not exist.
- **422 Unprocessable Entity:** The request body does not satisfy the validation rules.

## Data Storage

This project currently uses **in-memory storage** rather than a database. Tasks are stored temporarily while the application is running.

**Important:** All tasks are removed when the server restarts. A future version can use SQLite or PostgreSQL for permanent storage.

## Future Improvements

- Integrate a database such as PostgreSQL
- Add user registration and authentication
- Add task deadlines and priorities
- Implement pagination and filtering
- Add automated tests using Pytest
- Deploy the API to a cloud platform
- Add a frontend interface

## Learning Objectives

This project helps beginners understand:

- REST API concepts
- HTTP methods and status codes
- Request and response handling
- Data validation
- Error handling
- Backend server setup
- API testing with Postman
- Basic version control with Git

## License

This project is intended for educational and learning purposes. You may modify and extend it for your own practice.
