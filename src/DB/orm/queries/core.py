from sqlalchemy import text
from DB.orm.database import engine
from DB.orm.models import metadata_obj

async def create_tables():
    async with engine.begin() as conn: 
        await conn.run_sync(metadata_obj.create_all)