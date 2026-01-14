import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy import URL, create_engine, text

from DB.orm.models import metadata_obj
from DB.orm.config import settings

engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=True,
    pool_size=5,
    max_overflow=10,
    )

# test query 
async def get_version():
    async with engine.connect() as conn:
        res = await conn.execute(text("SELECT VERSION()"))
        version = res.scalar()
        print(version)

async def main():
    await get_version()

if __name__ == '__main__':
    asyncio.run(main())