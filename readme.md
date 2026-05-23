# FastAPI Production Todo API

A production-style Todo Backend API built using FastAPI, SQLAlchemy ORM, JWT Authentication, RBAC, and layered backend architecture.

This project demonstrates real-world backend engineering concepts including authentication, authorization, middleware, dependency injection, ORM-based database handling, and scalable project structure.

---

# Tech Stack

- FastAPI
- SQLAlchemy ORM
- SQLite / PostgreSQL
- JWT Authentication
- Passlib (bcrypt)
- Pydantic
- Role-Based Access Control (RBAC)

---

# Features

## Authentication
- User Registration
- User Login
- Password Hashing
- JWT Token Generation
- Protected Routes

## Authorization
- Role-Based Access Control
- Admin & User Roles
- Ownership Validation
- Only Admin Can Delete Todos

## Todo Management
- Create Todo
- Get All Todos
- Get Single Todo
- Update Todo
- Delete Todo
- Todo Status Tracking

## Middleware
- Request Logging Middleware
- Request Processing Time
- Response Status Logging

## Backend Architecture
- Layered Architecture
- Service Layer Pattern
- Dependency Injection
- Clean Separation of Concerns

---

# Project Structure

app/
│
├── main.py
│
├── routes/
│   ├── auth_routes.py
│   └── todo_routes.py
│
├── services/
│   ├── auth_service.py
│   └── todo_service.py
│
├── schemas/
│   ├── auth_schema.py
│   └── todo_schema.py
│
├── models/
│   ├── user_model.py
│   └── todo_model.py
│
├── database/
│   ├── db.py
│   └── base.py
│
├── middleware/
│   └── logging_middleware.py
│
├── core/
│   ├── config.py
│   ├── security.py
│   └── dependencies.py
│
└── requirements.txt

---

# API Features

## Auth APIs

### Register User
POST /auth/register

### Login User
POST /auth/login

---

## Todo APIs

### Create Todo
POST /todos

### Get All Todos
GET /todos

### Get Single Todo
GET /todos/{todo_id}

### Update Todo
PUT /todos/{todo_id}

### Delete Todo
DELETE /todos/{todo_id}

---

# Authentication Flow

1. User Registers
2. Password gets hashed
3. User logs in
4. JWT token generated
5. Client sends token in Authorization header
6. Protected routes validate token

Authorization Header:

Bearer YOUR_ACCESS_TOKEN

---

# RBAC (Role-Based Access Control)

## User Role
- Create Todo
- View Todo
- Update Own Todo

## Admin Role
- All User Permissions
- Delete Todos
- Manage All Todos

---

# Todo Status System

Supported statuses:
- pending
- in_progress
- completed

---

# Database

The project supports:
- SQLite (development)
- PostgreSQL (production)

ORM used:
- SQLAlchemy

---

# Dependency Injection

FastAPI Depends() is used for:
- Database Session Injection
- Current User Injection
- Authorization Injection

---

# Middleware

Custom logging middleware logs:
- HTTP Method
- Request URL
- Response Status
- Processing Time

---

# Installation

## Clone Repository

git clone https://github.com/your-username/fastapi-production-todo-api.git

cd fastapi-production-todo-api

---

# Create Virtual Environment

## Windows

python -m venv venv

venv\Scripts\activate

---

# Install Dependencies

pip install -r requirements.txt

---

# Run Server

uvicorn app.main:app --reload

---

# Swagger API Docs

http://127.0.0.1:8000/docs

---

# Sample Create Todo Request

{
  "title": "Learn FastAPI",
  "description": "Build production backend APIs"
}

---

# Production Concepts Implemented

- REST API Design
- ORM Architecture
- JWT Authentication
- Authorization
- RBAC
- Middleware
- Dependency Injection
- SQLAlchemy ORM
- Database Session Handling
- Clean Architecture
- Backend Service Layer
- API Validation
- Protected Routes

---

# Future Improvements

- Alembic Migrations
- Docker Support
- Redis Caching
- Async SQLAlchemy
- Refresh Tokens
- Pagination
- Search & Filtering
- Unit Testing
- CI/CD Pipeline
- Structured Logging
- PostgreSQL Optimization
- API Rate Limiting

---

# Learning Outcomes

This project helps understand:
- FastAPI Backend Development
- Real Backend Architecture
- Authentication & Authorization
- SQLAlchemy ORM
- JWT Workflow
- Middleware
- Database Design
- Dependency Injection
- API Security

---

# Author

Manu Singh

Backend Engineer | FastAPI | Django | GenAI | SQLAlchemy
