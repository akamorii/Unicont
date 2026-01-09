# from DB.db_init import pool
from fastapi import Request
import json

async def add_task(request:Request, name, description, body, answer):
    async with request.app.state.pool.acquire() as conn:
        await conn.execute(
            """
            INSERT INTO tasks (name, description, body, answer)
            VALUES ($1, $2, $3, $4)
            """,
            name, description, body, json.dumps(answer)
        )


async def get_task(request:Request,task_id):
    async with request.app.state.pool.acquire() as conn:
        row = await conn.fetchrow(
            "SELECT * FROM tasks WHERE id = $1",
            task_id
        )
        return dict(row) if row else None