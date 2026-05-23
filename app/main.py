from fastapi import FastAPI

from app.database.db import Base, engine

from app.routes.auth_routes import router as auth_router

from app.routes.todo_routes import router as todo_router

from app.middleware.logging_middleware import (
    LoggingMiddleware
)

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(LoggingMiddleware)

app.include_router(auth_router)

app.include_router(todo_router)