from typing import Annotated

import sys
import os

# sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from fastapi import FastAPI, Path
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pydantic import BaseModel, HttpUrl

# from sites.views import router as sites_router

app = FastAPI()

# app.include_router(sites_router)

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