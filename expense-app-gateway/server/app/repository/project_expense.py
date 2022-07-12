from datetime import datetime
from pyexpat import model
import uuid


from pydantic import BaseModel
from typing import Optional
import uuid
import datetime
from app.repository import project_expense_db
from app.models import project_expense as project_expense_model




class ProjectExpenseRepository():
    def __init__(self):
        pass
    def create_project_expense(self, project_expense: project_expense_model.ProjectExpense):
        return project_expense_db.create_project_expense(project_expense)
    def get_one_project_expense(self, project_expense_id):
        return project_expense_db.get_one_project_expense(project_expense_id)
    def get_all_project_expense_paginated(self, page_number, page_size):
        return project_expense_db.get_all_project_expense_paginated(page_number, page_size)
    def update_project_expense(self, project_expense_id, project_expense: project_expense_model.ProjectExpense):
        return project_expense_db.update_project_expense(project_expense_id, project_expense)
    def delete_project_expense(self, project_expense_id):
        return project_expense_db.delete_project_expense(project_expense_id)
    