from typing import Annotated

from enum import Enum

import sys
import os

# sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from fastapi import FastAPI, Path
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pydantic import BaseModel, HttpUrl

app = FastAPI()

# app.include_router(sites_router)

# Настройка CORS
#TODO почитать про CORS и middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # Разрешить все домены (для разработки)
    allow_credentials=True,
    allow_methods=['*'],  # Разрешить все методы (GET, POST, PUT и т.д.)
    allow_headers=['*'],  # Разрешить все заголовки
)

class users(int, Enum):
    alexandr = 1
    artem = 2
    zxc = 3 

@app.get('/')
async def root():
    return {'item_id': 'hello','name': 'aka','price': '1488'}
    
    
@app.get('/user/{user_id}')
async def get_user_by_id(user_id: users,query_2: int,  query: int = 10):
    return {'user': {user_id.name},
            'q': query,
            'q_2': query_2}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
    

