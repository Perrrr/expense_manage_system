from optparse import OptParseError
from turtle import update
from pydantic import BaseModel
from typing import Literal, Optional
from datetime import datetime

class DepartmentCategoryBudget(BaseModel):
    department_category_budget_id : Optional[int] = None
    department_id : int
    category_budget_id : str
    status : str
    created_at : datetime
    updated_at : datetime
    deleted_at : datetime

