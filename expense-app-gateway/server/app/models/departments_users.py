from turtle import update
from pydantic import BaseModel
from typing import Literal, Optional
from datetime import datetime

class DepartmentsUsers(BaseModel):
    department_user_id : Optional[int] = None
    department_id : int
    user_id : int
    created_at : datetime
    updated_at : datetime
    deleted_at : datetime
    
class CreateDepartmentUserForm(BaseModel):
    department_id : int
    user_id : int
    class Config: 
        schema_extra ={
            "example" : {
                "department_id" : 1,
                "user_id" : 1
            }
            
        }
    