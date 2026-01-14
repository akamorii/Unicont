from sqlalchemy import text, insert
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from DB.orm.database import engine
from DB.orm.models import metadata_obj, tasks_table


async def create_tables():
    async with engine.begin() as conn: 
        await conn.run_sync(metadata_obj.create_all)
        

async def insert_task():
    async with engine.connect() as conn:
        stmt = insert(tasks_table).values(
            [
                {"name":"qwerty","description":"qwerty","body":"zxc","answer":{"x_1":1, "x_2":4}}
            ]
        )
        await conn.execute(stmt)
        await conn.commit()
        
