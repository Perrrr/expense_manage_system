from turtle import update
from pydantic import BaseModel
from typing import Literal, Optional
from datetime import datetime

class OrganizationsUsers(BaseModel):
    organization_user_id : Optional[int] = None
    organization_id : int
    application_id : int
    user_id : int
    created_at : datetime
    updated_at : datetime
    deleted_at : datetime
    
    
class CreateOrganizationUserForm(BaseModel):
    organization_id : int
    application_id : int
    user_id :int
    class Config:
        schema_extra = {
        "example":
            {
            "organization_id" : 1,
            "application_id" : 1,
            "user_id" : 1,
        } 
  }
    