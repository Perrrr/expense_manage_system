from turtle import update
from pydantic import BaseModel
from typing import Literal, Optional
from datetime import datetime

class RolesPermissions(BaseModel):
    role_permission_id : Optional[int] = None
    application_id : int
    role_id : int
    permission_id : int
    created_at : datetime
    updated_at : datetime
    deleted_at : datetime
    
class CreateRolePermissionForm(BaseModel):
    application_id : int
    role_id : int
    permission_id : int
    class Config:
        schema_extra = {
            "example":
                {
                    "application_id" : 1,
                    "role_id" : 1,
                    "permission_id" : 1                  
                
            }
        }
    