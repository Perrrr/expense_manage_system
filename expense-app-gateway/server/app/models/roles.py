from turtle import update
from pydantic import BaseModel
from typing import Literal, Optional
from datetime import datetime

class Roles(BaseModel):
    role_id : Optional[int] = None
    public_id : Optional[str] = None
    application_id : int
    name : str
    description : str
    created_at : datetime
    updated_at : datetime
    deleted_at : datetime

class CreateRoleForm(BaseModel):
    public_id : Optional[str] = None
    application_id : int
    name : str
    description : str
    class Config:
        schema_extra = {
            "example":
                {
                    "application_id" : 1,
                    "name" : "test",
                    "description" : "test"
                }
        }