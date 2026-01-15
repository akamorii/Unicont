
"""
This file is needed to create models, aka tables, in the database.
"""
from typing import Annotated
import datetime
from json import dumps
from sqlalchemy import Table, Column, Integer, String, MetaData, JSON, text
from sqlalchemy.orm import Mapped, mapped_column
from DB.orm.database import Base


metadata_obj = MetaData()
 
intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE(('utc'), now())"))]
updated_at = Annotated[datetime.datetime, 
                       mapped_column( server_default=text("TIMEZONE(('utc'), now())"),
                                     onupdate=datetime.datetime.utcnow)
]
class Tasks_orm(Base):
    __tablename__ = "tasks"
    id: Mapped[intpk]
    name: Mapped[str] = mapped_column(String(60))
    description: Mapped[str] = mapped_column(default="test description")
    body: Mapped[str] = mapped_column(default="test body")
    # TODO добавить dumps при вставке
    answer: Mapped[dict] = mapped_column(JSON, default=lambda:{"test answer 1":1, "test answer 2": 2})
    
    
class Users_orm(Base):
    __tablename__ = "users"
    
    id: Mapped[intpk]
    username: Mapped[str] = mapped_column(String(30))
    bio: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(60))
    password: Mapped[str] = mapped_column(String(64))
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]


# tasks_table = Table(
#     "tasks",
#     metadata_obj,
#     Column("id", Integer, primary_key=True),
#     Column("name", String),
#     Column("description", String),
#     Column("body", String),
#     Column("answer", JSON)
# )
