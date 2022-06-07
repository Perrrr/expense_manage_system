from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Users(BaseModel):
    user_id : Optional[int] = None 
    public_id : Optional[str] = None
    email : str
    prefix_mobile : str
    mobile_number : str 
    activated : bool 
    created_at : datetime
    updated_at : datetime
    deleted_at : datetime

class CreateUserForm(BaseModel):
    public_id : Optional[str] = None
    email : str
    prefix_mobile : str
    mobile_number : str 
    activated : bool 
  