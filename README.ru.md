# Task Tracker API

- 🇬🇧 [English](README.md) | 🇷🇺 Русский

REST API для управления проектами и задачами, построенный на Django REST Framework + PostgreSQL.

---

## 🚀 Возможности

- JWT аутентификация (получение / обновление токенов)
- CRUD для проектов и задач
- Статусы задач: `todo`, `in_progress`, `done`
- Вложенные эндпоинты: задачи внутри проекта (`/api/projects/{id}/tasks/`)
- Фильтрация задач по проекту и статусу
- Поиск по проектам и задачам
- Пагинация
- Изоляция данных по пользователю (каждый видит только свои проекты и задачи)
- Docker-контейнеризация

---

## 🧱 Стек технологий

- Python 3.11+
- Django + Django REST Framework 3.16
- PostgreSQL
- SimpleJWT
- Docker + Docker Compose

---

## 🔐 Аутентификация

Проект использует JWT аутентификацию.

### Получить токен:
```
POST /api/token/
```
```json
{
  "username": "user",
  "password": "password"
}
```

### Обновить токен:
```
POST /api/token/refresh/
```

Добавляйте токен в каждый запрос:
```
Authorization: Bearer <access_token>
```

---

## 📂 API Эндпоинты

### Проекты
```
GET     /api/projects/
POST    /api/projects/
GET     /api/projects/{id}/
PUT     /api/projects/{id}/
PATCH   /api/projects/{id}/
DELETE  /api/projects/{id}/
```

### Задачи
```
GET     /api/tasks/
POST    /api/tasks/
GET     /api/tasks/{id}/
PUT     /api/tasks/{id}/
PATCH   /api/tasks/{id}/
DELETE  /api/tasks/{id}/
```

### Задачи проекта (nested)
```
GET     /api/projects/{id}/tasks/
```

### Фильтрация и поиск
```
/api/tasks/?project=1
/api/tasks/?status=todo
/api/tasks/?project=1&status=in_progress
/api/projects/?search=название
/api/tasks/?search=текст
```

### Пагинация
```
/api/tasks/?page=2
```

---

## ⚡ Быстрый старт (Docker)

```bash
git clone <repo>
cd task_tracker
cp .env.example .env
docker-compose up --build
```

Применить миграции (один раз):
```bash
docker-compose exec web python manage.py migrate
```

Создать суперпользователя (один раз):
```bash
docker-compose exec web python manage.py createsuperuser
```

После запуска API доступно по адресу:
- API: http://localhost:8000

---

## ⚙️ Установка без Docker

```bash
git clone <repo>
cd task_tracker
```

### Создать виртуальное окружение
```bash
python -m venv venv
source venv/bin/activate  # mac/linux
venv\Scripts\activate     # windows
```

### Установить зависимости
```bash
pip install -r requirements.txt
```

### Применить миграции
```bash
python manage.py migrate
```

### Создать суперпользователя
```bash
python manage.py createsuperuser
```

### Запустить сервер
```bash
python manage.py runserver
```

---

## 🗂 Структура проекта

```
task_tracker/
│
├── manage.py
├── config/            # Настройки Django, URLs
├── api/               # Модели Project и Task, ViewSets, сериализаторы
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .env
```

---

## 🧠 Архитектурные решения

- Плоские и вложенные эндпоинты сосуществуют с разными зонами ответственности: `/api/tasks/` — для глобального поиска и фильтрации, `/api/projects/{id}/tasks/` — для работы в контексте конкретного проекта
- Изоляция данных реализована через object-level permissions: пользователь получает доступ только к своим объектам, даже если знает чужой ID
- Статусы задач намеренно ограничены тремя значениями (`todo`, `in_progress`, `done`), чтобы упростить фильтрацию и не усложнять логику без необходимости

---

## 📌 Планы по развитию

- Дедлайны и приоритеты задач
- Назначение задач другим пользователям (совместная работа)
- Уведомления о приближающихся дедлайнах через email или Telegram

---

## 🎯 Цель проекта

Построен как портфельный backend-проект для демонстрации:

- Проектирования REST API с Django REST Framework
- JWT аутентификации и разграничения доступа на уровне объектов
- Работы с вложенными ресурсами и фильтрацией
- Docker-контейнеризации

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