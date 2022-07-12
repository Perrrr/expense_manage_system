from turtle import update
from pydantic import BaseModel
from typing import Literal, Optional
from datetime import datetime

class Departments(BaseModel):
    department_id : Optional[int] = None
    public_id : Optional[str] = None
    organization_id : int
    name : str
    description : str
    created_at : datetime
    updated_at : datetime
    deleted_at : datetime
    
class CreateDepartmentForm(BaseModel):
    public_id : Optional[str] = None
    organization_id : int
    name : str
    description : str
    class Config:
        schema_extra = {
        "example":
            {
            "organization_id" : 1,
            "name" : "Poramat Saichoo",
            "description" : "test",
        } 
  }
    