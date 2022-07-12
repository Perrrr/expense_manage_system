from datetime import datetime
import uuid

from pydantic import BaseModel
from typing import Optional
import uuid
import datetime
from app.service import expense_catagories_service
from app.models import expense_catagories as expense_catagorie_model



class ExpenseCatagoriesService():
    def __init__(self):
        pass
    def CreateExpenseCaragorie(self, expense_caragorie: expense_catagorie_model.CreateExpenseCatagoriesForm):
        return expense_catagories_service.CreateExpenseCatagorie(expense_caragorie)
    def GetOneExpenseCaragorie(self, expense_caragorie_id):
        return expense_catagories_service.GetOneExpenseCatagorie(expense_caragorie_id)
    def GetAllExpenseCaragoriesPaginated(self, page_number, page_size):
        return expense_catagories_service.GetAllExpenseCaragoriesPaginated(page_number, page_size)
    def UpdateExpenseCaragorie(self, expense_caragorie_id, expense_caragorie: expense_catagorie_model.CreateExpenseCatagoriesForm):
        return expense_catagories_service.UpdateExpenseCaragorie(expense_caragorie_id, expense_caragorie)
    def DeleteExpenseCaragorie(self, expense_caragorie_id):
        return expense_catagories_service.DeleteExpenseCatagorie(expense_caragorie_id)
        
