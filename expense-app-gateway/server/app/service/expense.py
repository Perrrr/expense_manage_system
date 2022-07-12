from datetime import datetime
import uuid

from pydantic import BaseModel
from typing import Optional
import uuid
import datetime
from app.service import expense_service
from app.models import expense as expense_model



class ExpenseService():
    def __init__(self):
        pass
    def CreateExpense(self, expense: expense_model.CreateExpenseForm):
        return expense_service.CreateExpense(expense)
    def GetOneExpense(self, expense_id):
        return expense_service.GetOneExpense(expense_id)
    def GetAllExpensesPaginated(self, page_number, page_size):
        return expense_service.GetAllExpensesPaginated(page_number, page_size)
    def UpdateExpense(self, expense_id, expense: expense_model.CreateExpenseForm):
        return expense_service.UpdateExpense(expense_id, expense)
    def DeleteExpense(self, expense_id):
        return expense_service.DeleteExpense(expense_id)
        
