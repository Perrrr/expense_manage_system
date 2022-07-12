from turtle import update
from pydantic import BaseModel
from typing import Literal, Optional
from datetime import datetime

class Projects(BaseModel):
    project_id : Optional[int] = None
    code : str
    public_id : Optional[str] = None
    organization_id : int
    avatar_color : str
    avatar_icon : str
    name : str
    description : str
    status : str
    created_at : datetime
    updated_at : datetime
    deleted_at : datetime

class CreateProjectForm(BaseModel):
    code : str
    public_id : Optional[str] = None
    organization_id : int
    avatar_color : str
    avatar_icon : str
    name : str
    description : str
    status : str
    class Config:
        schema_extra = {
            "example":
                {
                "code" : "test",
                "organization_id" : 1,
                "avatar_color" : "test",
                "avatar_icon" : "test",
                "name" : "test",
                "description" : "test",
                "status" : "test"
            }
        }
    