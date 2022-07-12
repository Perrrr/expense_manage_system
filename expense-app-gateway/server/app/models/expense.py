from turtle import update
from pydantic import BaseModel
from typing import Literal, Optional
from datetime import datetime

class Expense(BaseModel) :
    expense_id : Optional[int] = None
    public_id : Optional[str] = None
    expense_category_id : int
    cliam_reimbursement : bool
    description : str
    reference_number : str
    currency_id : int
    merchant_id : int
    amount : float
    user_id : int
    created_at : datetime
    updated_at : datetime
    deleted_at : datetime
    
class CreateExpenseForm(BaseModel):
    public_id : Optional[str] = None
    expense_category_id : int
    cliam_reimbursement : bool
    description : str
    reference_number : str
    currency_id : int
    merchant_id : int
    amount : float
    user_id : int
    class Config:
        schema_extra = {
        "example":
            {
            "expense_category_id" : 1,
            "cliam_reimbursement" : False,
            "description" : "test",
            "reference_number" : "456456",
            "currency_id" : 1,
            "merchant_id" : 1,
            "amount" : 1.00,
            "user_id" : 1
        } 
    }