
from pydantic import BaseModel
from typing import Literal, Optional
from datetime import datetime

class Currencies(BaseModel):
    currencies_id : Optional[int] = None
    public_id : Optional[str] = None
    organization_id : int
    name : str
    code : str
    symbol : str
    created_at : datetime
    updated_at : datetime
    deleted_at : datetime
    
class CreateCurrencieForm(BaseModel):
    public_id : Optional[str] = None
    organization_id : int
    name : str
    code : str
    symbol : str
    class Config:
        schema_extra = {
        "example":
            {
            "organization_id" : 88,
            "name" : "TNT",
            "code" : "9955777",
            "symbol" : "Tri" 
        } 
  }