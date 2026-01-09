# from DB.db_init import pool
from fastapi import Request
import json
from pydantic import BaseModel, Field

async def add_task(request:Request, name, description, body, answer):
    async with request.app.state.pool.acquire() as conn:
        await conn.execute(
            """
            INSERT INTO tasks (name, description, body, answer)
            VALUES ($1, $2, $3, $4)
            """,
            name, description, body, json.dumps(answer)
        )


async def get_tasks(request:Request, limit, offset):
    async with request.app.state.pool.acquire() as conn:
        rows = await conn.fetch(
            "SELECT * FROM tasks WHERE id < $1 AND id > $2",
            limit, offset
        )
    return rows if rows else None

    

async def update_task(request:Request, updateble_task_id, updateble_fields):
    pass