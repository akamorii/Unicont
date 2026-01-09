from tasks.schemas import Task
from fastapi import Request

if __name__ != '__main__':
    from DB.tasks_db import add_task, get_tasks
    
import asyncio


async def create_task(request:Request, task: Task):
    dict_task = dict(task)
    await add_task(request,**dict_task)
    return {
        "status": "succsseful",
        "message": "task successuful added",
        "added_task": dict_task
    }
    
async def show_tasks(request:Request, limit, offset):
    tasks = await get_tasks(request, limit, offset)
    return tasks
    

if __name__ == '__main__':
    
    linear_eq = {
        "name": "linear equation",
        "description": "easy linear equation",
        "body": r"$$\begin{cases}x + y = 10 \\ 2x - y = 8\end{cases}$$",
        "answer": {"x": 6, "y": 4},
    }
    # print(Task(**linear_eq))
    asyncio.run(create_task(Task(**linear_eq)))