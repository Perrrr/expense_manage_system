from app.repository import department_budget_db
from app.models import department_budget as department_budget_model

class DepartmentBudgetRepository():
    def __init__(self):
        pass
    def create_department_budget(self, department_budget: department_budget_model.DepartmentBudget):
        return department_budget_db.create_department_budget(department_budget)
    def get_one_department_budget(self, department_budget_id):
        return department_budget_db.get_one_department_budget(department_budget_id)
    def get_all_department_budget_paginated(self, page_number, page_size):
        return department_budget_db.get_all_department_budget_paginated(page_number, page_size)
    def update_department_budget(self, department_budget_id, department_budget: department_budget_model.DepartmentBudget):
        return department_budget_db.update_department_budget(department_budget_id,department_budget)
    def delete_departmnet_budget(self, department_budget_id):
        return department_budget_db.delete_department_budget(department_budget_id)
    
    