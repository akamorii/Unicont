import asyncpg
from dotenv import load_dotenv
from os import getenv

load_dotenv()

pool: asyncpg.Pool | None = None


async def init_db(app):
    app.state.pool = await asyncpg.create_pool(
        host=getenv("DB_ADRESS"),
        port=int(getenv("DB_PORT")),
        user=getenv("DB_USER"),
        password=getenv("DB_PASS"),
        database=getenv("DB_NAME"),
        min_size=1,
        max_size=10,
    )


async def close_db(app):
    await app.state.pool.close()


async def create_tables(app):
    async with app.state.pool.acquire() as conn:
        await conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            name VARCHAR(80),
            description TEXT,
            body TEXT,
            answer JSONB
        );
        """)