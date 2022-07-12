from optparse import OptParseError
from turtle import update
from pydantic import BaseModel
from typing import Literal, Optional
from datetime import datetime

class DepartmentBudget(BaseModel):
    department_budget_id : Optional[int] = None
    budget_id : int
    department_id : int
    status : str
    created_at : datetime
    updated_at : datetime
    deleted_at : datetime

