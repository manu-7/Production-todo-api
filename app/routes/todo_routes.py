from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.todo_schema import (
    TodoCreate,
    TodoUpdate
)

from app.services.todo_service import *

from app.core.dependencies import (
    get_db,
    get_current_user,
    admin_only
)

router = APIRouter(
    prefix="/todos",
    tags=["Todos"]
)

@router.post("/")
def create(
    todo: TodoCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    return create_todo(
        db,
        todo,
        current_user["user_id"]
    )


@router.get("/")
def get_all(
    db: Session = Depends(get_db)
):

    return get_all_todos(db)


@router.get("/{todo_id}")
def get_one(
    todo_id: int,
    db: Session = Depends(get_db)
):

    return get_single_todo(db, todo_id)


@router.put("/{todo_id}")
def update(
    todo_id: int,
    todo: TodoUpdate,
    db: Session = Depends(get_db)
):

    return update_todo(
        db,
        todo_id,
        todo
    )


@router.delete("/{todo_id}")
def delete(
    todo_id: int,
    db: Session = Depends(get_db),
    admin = Depends(admin_only)
):

    return delete_todo(db, todo_id)