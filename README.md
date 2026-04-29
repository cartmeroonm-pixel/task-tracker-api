# Task Tracker API

- 🇬🇧 English | 🇷🇺 [Русский](README.ru.md)

REST API for project and task management built with Django REST Framework + PostgreSQL.

---

## 🚀 Features

- JWT authentication (access / refresh tokens)
- Full CRUD for projects and tasks
- Task statuses: `todo`, `in_progress`, `done`
- Nested endpoints: tasks scoped to a project (`/api/projects/{id}/tasks/`)
- Task filtering by project and status
- Search across projects and tasks
- Pagination
- User-based data isolation (each user sees only their own projects and tasks)
- Dockerized setup

---

## 🧱 Tech Stack

- Python 3.11+
- Django + Django REST Framework 3.16
- PostgreSQL
- SimpleJWT
- Docker + Docker Compose

---

## 🔐 Authentication

This project uses JWT authentication.

### Get token:
```
POST /api/token/
```
```json
{
  "username": "user",
  "password": "password"
}
```

### Refresh token:
```
POST /api/token/refresh/
```

Include the token in every request:
```
Authorization: Bearer <access_token>
```

---

## 📂 API Endpoints

### Projects
```
GET     /api/projects/
POST    /api/projects/
GET     /api/projects/{id}/
PUT     /api/projects/{id}/
PATCH   /api/projects/{id}/
DELETE  /api/projects/{id}/
```

### Tasks
```
GET     /api/tasks/
POST    /api/tasks/
GET     /api/tasks/{id}/
PUT     /api/tasks/{id}/
PATCH   /api/tasks/{id}/
DELETE  /api/tasks/{id}/
```

### Tasks scoped to a project (nested)
```
GET     /api/projects/{id}/tasks/
```

### Filtering and search
```
/api/tasks/?project=1
/api/tasks/?status=todo
/api/tasks/?project=1&status=in_progress
/api/projects/?search=name
/api/tasks/?search=text
```

### Pagination
```
/api/tasks/?page=2
```

---

## ⚡ Quick Start (Docker)

```bash
git clone <repo>
cd task_tracker
cp .env.example .env
docker-compose up --build
```

Apply migrations (once):
```bash
docker-compose exec web python manage.py migrate
```

Create a superuser (once):
```bash
docker-compose exec web python manage.py createsuperuser
```

Once running:
- API: http://localhost:8000

---

## ⚙️ Installation (without Docker)

```bash
git clone <repo>
cd task_tracker
```

### Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # mac/linux
venv\Scripts\activate     # windows
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Apply migrations
```bash
python manage.py migrate
```

### Create superuser
```bash
python manage.py createsuperuser
```

### Run server
```bash
python manage.py runserver
```

---

## 🗂 Project Structure

```
task_tracker/
│
├── manage.py
├── config/            # Django settings, URLs
├── api/               # Project and Task models, ViewSets, serializers
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .env
```

---

## 🧠 Design Decisions

- Flat and nested endpoints coexist with distinct responsibilities: `/api/tasks/` is used for global search and filtering across all tasks, while `/api/projects/{id}/tasks/` provides tasks in the context of a specific project
- Data isolation is enforced via object-level permissions: a user can only access their own objects, even if they know someone else's ID
- Task statuses are intentionally limited to three values (`todo`, `in_progress`, `done`) to keep filtering simple and avoid unnecessary complexity

---

## 📌 Future Improvements

- Task deadlines and priorities
- Task assignment to other users (team collaboration)
- Notifications for approaching deadlines via email or Telegram

---

## 🎯 Project Purpose

Built as a backend portfolio project to demonstrate:

- REST API design with Django REST Framework
- JWT authentication and object-level permissions
- Working with nested resources and filtering
- Docker containerization

---

## 📄 .env.example

```
DEBUG=True
SECRET_KEY=your-secret-key

DB_NAME=task_tracker
DB_USER=postgres
DB_PASSWORD=your_db_password
DB_HOST=db
DB_PORT=5432
```