from turtle import update
from pydantic import BaseModel
from typing import Literal, Optional
from datetime import datetime

class Organizations(BaseModel):
    organization_id : Optional[int] = None
    public_id : Optional[str] = None
    name : str
    code : str
    avatar_icon : str
    avatar_color : str
    image_url : str
    description : str
    created_at : datetime
    updated_at : datetime
    deleted_at : datetime


class CreateOrganizationForm(BaseModel):
    public_id : Optional[str] = None
    name : str
    code : str
    avatar_icon : str
    avatar_color : str
    image_url : str
    description : str
    class Config:
        schema_extra = {
        "example":
            {
            "name" : "test",
            "code" : "test",
            "avatar_icon" : "test",
            "avatar_color" :"test",
            "image_url" : "test",
            "description": "test"         
        } 
  }