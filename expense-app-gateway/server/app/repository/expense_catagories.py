from datetime import datetime
import profile
from pyexpat import model
import uuid


from pydantic import BaseModel
from typing import Optional
import uuid
import datetime
from app.repository import expense_catagories_db
from app.models import expense_catagories as expense_catagorie_model




class ExpenseCatagoriesRepository():
    def __init__(self):
        pass
    def create_expense_catagories(self, expense_catagorie: expense_catagorie_model.ExpenseCatagories):
        return expense_catagories_db.create_expense_categories(expense_catagorie)
    def get_one_expense_catagorie(self, expense_catagorie_id):
        return expense_catagories_db.get_one_expense_catagorie(expense_catagorie_id)
    def get_all_expense_catagories_paginated(self, page_number, page_size):
        return expense_catagories_db.get_all_expense_categories_paginated(page_number, page_size)
    def update_expense_catagories(self, expense_catagorie_id, expense_catagorie: expense_catagorie_model.ExpenseCatagories):
        return expense_catagories_db.update_expense_categories(expense_catagorie_id, expense_catagorie)
    def delete_expense_catagories(self, expense_catagorie_id):
        return expense_catagories_db.delete_expense_categories(expense_catagorie_id)
    