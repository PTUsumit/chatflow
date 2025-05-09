from pydantic import BaseModel
from typing import List

class Task(BaseModel):
    id:int 
    title:str
    done: bool=False

class AppState(BaseModel):
    user_input:str
    last_command:str=''    