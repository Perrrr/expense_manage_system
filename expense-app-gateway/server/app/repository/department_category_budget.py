from app.repository import department_category_budget_db
from app.models import department_category_budget as department_category_budget_model

class DepartmentCategoryBudgetRepository():
    def __init__(self):
        pass
    def create_department_category_budget(self, department_category_budget: department_category_budget_model.DepartmentCategoryBudget):
        return department_category_budget_db.create_department_category_budget(department_category_budget)
    def get_one_department_category_budget(self, department_category_budget_id):
        return department_category_budget_db.get_one_department_category_budget(department_category_budget_id)
    def get_all_department_category_budget_paginated(self, page_number, page_size):
        return department_category_budget_db.get_all_department_category_budget_paginated(page_number,page_size)
    def update_department_category_budget(self, department_category_budget_id, department_category_budget: department_category_budget_model.DepartmentCategoryBudget):
        return department_category_budget_db.update_department_category_budget(department_category_budget_id, department_category_budget)
    def delete_department_category_budget(self, department_category_budget_id):
        return department_category_budget_db.delete_department_category_budget(department_category_budget_id)