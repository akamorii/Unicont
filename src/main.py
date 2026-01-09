from typing import Annotated
from contextlib import asynccontextmanager
import asyncio

import sys
import os
from tasks.views import router as task_router

from DB.db_init import init_db,create_tables, close_db
# sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from fastapi import FastAPI, Path
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pydantic import BaseModel, HttpUrl

# from sites.views import router as sites_router
@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db(app)
    await create_tables(app)
    yield
    await close_db(app)
app = FastAPI(lifespan=lifespan)

app.include_router(task_router)

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить все домены (для разработки)
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все методы (GET, POST, PUT и т.д.)
    allow_headers=["*"],  # Разрешить все заголовки
)


class MonitoredSite(BaseModel):
    addr: HttpUrl

@app.get('/')
async def root():
    return {}

# @app.get('/users')
# async def 
if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)