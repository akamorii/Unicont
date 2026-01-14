"""
In this file, the creation of the orm core occurs,
as well as the creation of templates that are somehow
related to the core (for example, sessions)
"""

import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy import URL, create_engine, text
from sqlalchemy.orm import DeclarativeBase

from DB.orm.config import settings

# engine (главная часть)
engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=True,
    pool_size=5,
    max_overflow=10,
    )


# -- шаблон создания сессий --
session_factory = async_sessionmaker(engine)

class Base(DeclarativeBase):
    pass
# -- end -- 



# # test query 
# async def get_version():
#     async with engine.connect() as conn:
#         res = await conn.execute(text("SELECT VERSION()"))
#         version = res.scalar()
#         print(version)



if __name__ == '__main__':
    pass