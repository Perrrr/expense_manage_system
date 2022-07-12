from optparse import OptParseError
from turtle import update
from pydantic import BaseModel
from typing import Literal, Optional
from datetime import datetime

class Budget(BaseModel):
    budget_id : Optional[int] = None
    public_id : Optional[str] = None
    budget : float
    note : Optional[str] = None
    budget_period : str
    currency_id : int
    created_at : datetime
    updated_at : datetime
    deleted_at : datetime