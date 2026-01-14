import asyncio
from DB.orm.queries.core import create_tables

asyncio.run(create_tables())