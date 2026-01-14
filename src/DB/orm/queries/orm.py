from sqlalchemy import text, insert
from DB.orm.database import engine, session_factory
from DB.orm.models import metadata_obj, Task_orm


async def create_task():
    task_eq = Task_orm(name="linear_equation_2")
    async with session_factory() as session:
        session.add(task_eq)
        await session.commit()