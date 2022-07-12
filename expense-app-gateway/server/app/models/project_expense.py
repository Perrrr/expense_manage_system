from turtle import update
from pydantic import BaseModel
from typing import Literal, Optional
from datetime import date, datetime

class ProjectExpense(BaseModel):
    project_expense_id : Optional[int] = None
    project_id : int
    expense_id : int
    created_at : datetime
    updated_at : datetime
    deleted_at : datetime
    
class CreateProjectExpenseForm(BaseModel): 
    project_id : int
    expense_id : int
    class Config :
        schema_extra = {
            "example":
                {
                    "project_id" : 1,
                    "expense_id" : 1
                }
        }