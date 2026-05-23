from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)

from app.database.db import Base

class Todo(Base):

    __tablename__ = "todos"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(
        String,
        nullable=False
    )

    description = Column(String)

    status = Column(
        String,
        default="pending"
    )

    owner_id = Column(
        Integer,
        ForeignKey("users.id")
    )