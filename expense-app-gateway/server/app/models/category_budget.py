from optparse import OptParseError
from turtle import update
from pydantic import BaseModel
from typing import Literal, Optional
from datetime import datetime

class CategoryBudget(BaseModel):
    category_budget_id : Optional[int] = None
    budget_id : int
    name : str
    status : str
    avatar_icon : str
    avatar_color : str
    image_url : str
    created_at : datetime
    updated_at : datetime
    deleted_at : datetime

