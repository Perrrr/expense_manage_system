from turtle import update
from pydantic import BaseModel
from typing import Literal, Optional
from datetime import datetime

class Merchant(BaseModel):
    merchant_id : Optional[int] = None
    name : str
    description : str
    created_at : datetime
    updated_at : datetime
    deleted_at : datetime

class CreateMerchantForm(BaseModel):
    name : str
    description : str
    class Config:
        schema_extra = {
        "example":
            {
            "name" : "Phunara Ry",
            "description" : "test",
        } 
  }
 