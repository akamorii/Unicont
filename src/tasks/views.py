from fastapi import APIRouter, Request
from DB.tasks_db import get_task
from tasks.schemas import Task
from tasks.crud import create_task
router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("/get_task/{id}")
async def show_task(id):
    task = await get_task(id)
    return {"task": {
        "name": task[1],
        "description": task[2],
        "body": task[3],
        "answer": task[4]
    }}
    
    
@router.post("/add_task/")
async def show_task(request: Request,new_task: Task):
    return await create_task(request, new_task)
    
