from pydantic import BaseModel

class Task (BaseModel):
    name:str
    description:str
    body:str
    answer:dict