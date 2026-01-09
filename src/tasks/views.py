from fastapi import APIRouter, Request, Query
from tasks.schemas import Task
from DB.tasks_db import get_tasks
from tasks.crud import create_task, show_tasks

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("/get_task")
async def list_task(request: Request, limit:int = Query(20, ge=1, le=100), offset:int = Query(0, ge=0)):
    tasks = await show_tasks(request, limit, offset)
    return  {"ans": tasks}
    
    
@router.post("/add_task/")
async def add_task(request: Request,new_task: Task):
    return await create_task(request, new_task)
    
