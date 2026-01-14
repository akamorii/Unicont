
"""
This file is needed to create models, aka tables, in the database.
"""
from json import dumps
from sqlalchemy import Table, Column, Integer, String, MetaData, JSON
from sqlalchemy.orm import Mapped, mapped_column
from DB.orm.database import Base


metadata_obj = MetaData()
 

class Task_orm(Base):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(60))
    description: Mapped[str] = mapped_column(default="test description")
    body: Mapped[str] = mapped_column(default="test body")
    answer: Mapped[dict] = mapped_column(JSON, default=dumps({"test answer 1":1, "test answer 2": 2}))
    




# tasks_table = Table(
#     "tasks",
#     metadata_obj,
#     Column("id", Integer, primary_key=True),
#     Column("name", String),
#     Column("description", String),
#     Column("body", String),
#     Column("answer", JSON)
# )
