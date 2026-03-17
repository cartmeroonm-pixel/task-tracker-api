# Task Tracker API

Простой backend для управления проектами и задачами с использованием Django REST Framework и PostgreSQL.

---

## 🔹 Технологии

- Python 3.11+ (в Docker используется Python 3.11)
- Django (см. `requirements.txt`)
- Django REST Framework 3.16.1 
- PostgreSQL  
- Docker + docker-compose  
- JWT авторизация  

---

## 🔹 Функциональность

- CRUD для проектов и задач  
- Авторизация через JWT  
- Object-level permissions (пользователь видит только свои проекты/задачи)  
- Статусы задач: `todo`, `in_progress`, `done`  
- Docker-контейнеризация с Postgres  

---

## 🔹 Установка и запуск (Docker)

1. Клонировать репозиторий:

```bash
git clone <URL-репозитория>
cd task_tracker
```

2. Создать `.env` в корне проекта (можно взять за основу `.env.example`):

```env
DEBUG=True
SECRET_KEY=your_secret_key

DB_NAME=task_tracker
DB_USER=postgres
DB_PASSWORD=your_db_password
DB_HOST=db
DB_PORT=5432
```

Важно: значения `DB_NAME/DB_USER/DB_PASSWORD` используются и приложением, и контейнером Postgres (см. `docker-compose.yml`).

3. Запустить проект через Docker:

```bash
docker-compose up --build
```

4. Применить миграции (один раз):

```bash
docker-compose exec web python manage.py migrate
```

5. Создать суперпользователя (один раз):

```bash
docker-compose exec web python manage.py createsuperuser
```

6. API доступно по адресам:

```bash
http://localhost:8000/api/projects/
http://localhost:8000/api/tasks/
```

---

## 🔹 Примеры запросов

### Получение JWT токена

```bash
POST http://localhost:8000/api/token/
```

Body:

```json
{
  "username": "admin",
  "password": "your_password"
}
```

### CRUD проекты

```bash
GET http://localhost:8000/api/projects/
POST http://localhost:8000/api/projects/
```

Body: 

```json
{
    "name": "Новый проект"
}
```

### CRUD задачи

```bash
GET http://localhost:8000/api/tasks/
POST http://localhost:8000/api/tasks/
```

Body: 

```json
{
    "title": "Новая задача",
    "project": 1
}
```

Не забудьте добавить Bearer Token в заголовок `Authorization`.

Пример заголовка:

```bash
Authorization: Bearer <access_token>
```

---

## 🔹 Эндпоинты и полезные возможности

- **JWT**:
  - `POST /api/token/` — получить пару токенов
  - `POST /api/token/refresh/` — обновить access по refresh
- **Проекты**: `GET/POST /api/projects/`, `GET/PUT/PATCH/DELETE /api/projects/{id}/`
- **Задачи**: `GET/POST /api/tasks/`, `GET/PUT/PATCH/DELETE /api/tasks/{id}/`
- **Задачи проекта (nested)**: `GET /api/projects/{id}/tasks/`
- **Фильтры задач**: `GET /api/tasks/?project=<id>&status=todo`
- **Поиск**:
  - проекты: `GET /api/projects/?search=<name>`
  - задачи: `GET /api/tasks/?search=<text>`
- **Пагинация**: включена, параметр `page` (пример: `GET /api/tasks/?page=2`)

---

## 🔹 Структура проекта

```bash
task_tracker/
│
├── manage.py
├── config/            # Django settings/urls
├── api/               # приложение с моделями Project и Task + ViewSet/serializers
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .env
```

---

## 🔹 Контакты / Автор

Имя: Дмитрий (Neverdebug)

GitHub: https://github.com/cartmeroonm-pixel

Цель проекта: портфолио для junior backend разработчика