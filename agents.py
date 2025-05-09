from state import AppState
import db
import asyncio

def create_agent(state: AppState) -> AppState:
    asyncio.run(db.add_task(state.user_input))
    state.last_command = "create"
    return state

def list_agent(state: AppState) -> AppState:
    state.last_command = "list"
    return state

def delete_agent(state: AppState) -> AppState:
    try:
        task_id = int(state.user_input.split()[-1])
        asyncio.run(db.delete_task(task_id))
        state.last_command = f"delete {task_id}"
    except:
        state.last_command = "delete failed"
    return state

def update_agent(state: AppState) -> AppState:
    try:
        parts = state.user_input.split(":")
        task_id = int(parts[0].split()[-1])
        new_title = parts[1].strip()
        asyncio.run(db.update_task(task_id, new_title))
        state.last_command = f"update {task_id}"
    except:
        state.last_command = "update failed"
    return state
