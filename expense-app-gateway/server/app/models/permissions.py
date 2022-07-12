from email.mime import application
from turtle import update
from pydantic import BaseModel
from typing import Literal, Optional
from datetime import datetime

class Permissions(BaseModel):
    permission_id : Optional[int] = None
    application_id : int
    public_id : Optional[str] = None
    name : str
    method : str
    description : str
    created_at : datetime
    updated_at : datetime
    deleted_at : datetime

class CreatePermissionForm(BaseModel):
    application_id : int
    public_id : Optional[str] = None
    name : str
    method : str
    description : str
    class Config:
        schema_extra = {
            "example":
                {
                    "application_id" : 1,
                    "name" : "test",
                    "method" : "test",
                    "description" : "test"
                }
        }