import asyncio
from DB.orm.queries.orm import create_tables, create_task


asyncio.run(create_tables())