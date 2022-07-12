from pydantic import BaseModel
from typing import Literal, Optional
from datetime import datetime

class Users(BaseModel):
    user_id : Optional[int] = None 
    public_id : Optional[str] = None
    email : str
    prefix_mobile : str
    mobile_number : str 
    activated : bool
    last_accessed_at : datetime
    last_login_at : datetime
    is_online : bool
    failed_password_attempts : int 
    note : Optional[str] =None
    status : Literal['activate' , 'inactive'] = 'inactive'
    created_at : datetime
    updated_at : datetime
    deleted_at : datetime

class CreateUserForm(BaseModel):
    public_id : Optional[str] = None
    email : str
    prefix_mobile : str
    mobile_number : str 
    activated : bool
    note : Optional[str] = None
    class Config:
        schema_extra = {
        "example":
            {
            "email" : "panudet.@gmail.com",
            "prefix_mobile" : "66",
            "mobile_number" : "9955777",
            "activated" : False,
            "note" : ""
        } 
  }