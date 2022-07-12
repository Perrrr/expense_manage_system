from datetime import datetime
import profile
from pyexpat import model
import uuid


from pydantic import BaseModel
from typing import Optional
import uuid
import datetime
from app.repository import expense_db
from app.models import expense as expense_model




class ExpenseRepository():
    def __init__(self):
        pass
    def create_expense(self, expense: expense_model.Expense):
        return expense_db.create_expense(expense)
    def get_one_expense(self, expense_id):
        return expense_db.get_one_expense(expense_id)
    def get_all_expense_paginated(self, page_number, page_size):
        return expense_db.get_all_expense_paginated(page_number, page_size)
    def update_expense(self, expense_id, expense: expense_model.Expense):
        return expense_db.update_expense(expense_id,expense)
    def delete_expense(self, expense_id):
        return expense_db.delete_expense(expense_id)
    