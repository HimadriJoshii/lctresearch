from pydantic import BaseModel,Field,ConfigDict
from datetime import datetime

class TaskCreate(BaseModel):
    title:str=Field(max_length=255)
    completed:bool=False

class TaskResponse(TaskCreate):
    id:int
    created_at:datetime
    model_config = ConfigDict(from_attributes=True)

class TaskUpdate(BaseModel):
    title:str|None=None
    completed:bool|None=None




