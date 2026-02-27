from fastapi import FastAPI,Depends
from schemas import TaskCreate,TaskResponse,TaskUpdate
from typing import Annotated
from database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import select
import models
from fastapi import HTTPException

app=FastAPI()

@app.get('/')
def home():
     return {
        'hello':'leute'
    }

@app.get('/tasks/',response_model=list[TaskResponse])
def get_tasks(db:Annotated[Session,Depends(get_db)]):
    result=db.execute(select(models.Task))
    tasks=result.scalars().all()
    return tasks
   

@app.get('/tasks/{task_id}',response_model=TaskResponse)
def get_task(task_id:int,db:Annotated[Session,Depends(get_db)]):
    result=db.execute(select(models.Task).where(models.Task.id==task_id))
    task=result.scalars().first()
    if not task:
        raise HTTPException(status_code=404,detail=f'task with id {task_id} not found')
    return task

@app.post("/tasks/",response_model=TaskResponse)
def create_task(task:TaskCreate,db:Annotated[Session,Depends(get_db)]):
    new_task=models.Task(
        title=task.title,
        completed=task.completed
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@app.put('/tasks/{task_id}',response_model=TaskResponse)
def full_update_task(task_id:int,updated_data:TaskCreate,db:Annotated[Session,Depends(get_db)]):
    result=db.execute(select(models.Task).where(models.Task.id==task_id))
    task=result.scalars().first()
    if not task:
        raise HTTPException(status_code=404,detail=f'task with id {task_id} not found')
    task.title=updated_data.title
    task.completed=updated_data.completed
    db.commit()
    db.refresh(task)
    return task

@app.patch('/tasks/{task_id}',response_model=TaskResponse)
def partial_update_task(task_id:int,updated_data:TaskUpdate,db:Annotated[Session,Depends(get_db)]):
    result=db.execute(select(models.Task).where(models.Task.id==task_id))
    task=result.scalars().first()
    if not task:
        raise HTTPException(status_code=404,detail=f'task with id {task_id} not found')
    updated_data=updated_data.model_dump(exclude_unset=True)
    for key,value in updated_data.items():
        setattr(task,key,value)
    db.commit()
    db.refresh(task)
    return task

@app.delete('/tasks/{task_id}',status_code=204)
def delete_task(task_id:int,db:Annotated[Session,Depends(get_db)]):
    result=db.execute(select(models.Task).where(models.Task.id==task_id))
    task=result.scalars().first()
    if not task:
        raise HTTPException(status_code=404,detail=f'task with id {task_id} not found')
    db.delete(task)
    db.commit()
    return 







