from optparse import OptParseError
from turtle import update
from pydantic import BaseModel
from typing import Literal, Optional
from datetime import datetime

class Applications(BaseModel):
    application_id : Optional[int] = None
    public_id : Optional[str] = None
    name : str
    description : Optional[str] = None
    avatar_color : str
    avatar_icon : str
    created_at : datetime
    updated_at : datetime
    deleted_at : datetime
    
class CreateApplicationForm(BaseModel):
    public_id : Optional[str] = None
    name : str
    description : Optional[str] = None
    avatar_color : str
    avatar_icon : str
    class Config:
        schema_extra ={
            "example":
                {
                    "name" : "Triple",
                    "avatar_color" : "test",
                    "avatar_icon" : "test"
                }
        }
