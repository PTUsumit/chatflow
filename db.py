import motor.motor_asyncio
from state import Task

client= motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
db=client.todo_db
collection=db.tasks
async def get_all_tasks():
    cursor=collection.find({})
    return [Task(**doc)async for doc in cursor]

async def add_task(title:str):
    count=await collection.count_documents({})
    new_task=Task(id=count+1,title=title)
    await collection.insert_one(new_task.dict())
    return new_task

async def delete_task(task_id:int):
    await collection.delete_one({'id':task_id})

async def update_task(task_id:int, new_title:str):
    await collection.update_one({'id':task_id},{'$set':{'title':new_title}})    