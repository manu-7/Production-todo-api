from sqlalchemy.orm import Session
from app.models.todo_model import Todo


def create_todo(
    db: Session,
    todo_data,
    user_id
):

    todo = Todo(
        title=todo_data.title,
        description=todo_data.description,
        owner_id=user_id
    )

    db.add(todo)

    db.commit()

    db.refresh(todo)

    return todo


def get_all_todos(db: Session):

    return db.query(Todo).all()


def get_single_todo(
    db: Session,
    todo_id
):

    return db.query(Todo).filter(
        Todo.id == todo_id
    ).first()


def update_todo(
    db: Session,
    todo_id,
    todo_data
):

    todo = db.query(Todo).filter(
        Todo.id == todo_id
    ).first()

    if not todo:
        return None

    if todo_data.title:
        todo.title = todo_data.title

    if todo_data.description:
        todo.description = todo_data.description

    if todo_data.status:
        todo.status = todo_data.status

    db.commit()

    db.refresh(todo)

    return todo


def delete_todo(
    db: Session,
    todo_id
):

    todo = db.query(Todo).filter(
        Todo.id == todo_id
    ).first()

    if not todo:
        return None

    db.delete(todo)

    db.commit()

    return True