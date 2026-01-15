from sqlalchemy import text, insert
from DB.orm.database import engine, session_factory
from DB.orm.models import Base, Tasks_orm


async def create_tables():
    async with engine.begin() as conn: 
        await conn.run_sync(Base.metadata.create_all)
        await conn.commit()
        

async def create_task():
    task_eq = Tasks_orm(name="linear_equation_2")
    async with session_factory() as session:
        session.add(task_eq)
        await session.commit()