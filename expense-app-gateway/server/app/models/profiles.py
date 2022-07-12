from turtle import update
from pydantic import BaseModel
from typing import Literal, Optional
from datetime import datetime

class Profiles(BaseModel):
    profile_id : Optional[int] = None
    user_id : int
    first_name : str
    last_name : str
    avatar_icon : str
    avatar_color : str
    image_url : str
    created_at : datetime
    updated_at : datetime
    deleted_at : datetime
    
class CreateProfileForm(BaseModel):
    user_id : int
    first_name : str
    last_name : str
    avatar_icon : str
    avatar_color : str
    image_url : str
    class Config:
        schema_extra = {
            "example":
                {
                    "user_id" : 1,
                    "first_name" : "panudet",
                    "last_name" : "panumas",
                    "avatar_icon" : "141216.jpg",
                    "avatar_color" : "#FF5733",
                    "image_url" : "test.com/test"
                }
        }

