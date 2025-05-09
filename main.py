from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
from state import AppState
from graph import build_graph
import db

app= FastAPI()
graph=build_graph()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)

class InputModel(BaseModel):
    query: str

@app.post('/process')
async def process(data: InputModel):
    state=AppState(user_input=data.query)
    new_state=graph.invoke(state)
    tasks=await db.get_all_tasks()
    return {"tasks": [task.dict() for task in tasks],
            'last_comand':new_state.last_command}