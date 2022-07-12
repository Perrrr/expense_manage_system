from app.repository import category_budget_db
from app.models import category_budget as category_budget_model

class CategoryBudgetRepository():
    def __init__(self):
        pass
    def create_category_budget(self, category_budget: category_budget_model.CategoryBudget):
        return category_budget_db.create_category_budget(category_budget)
    def get_one_category_budget(self, category_budget_id):
        return category_budget_db.get_one_category_budget(category_budget_id)
    def get_all_category_budget_paginated(self, page_number, page_size):
        return category_budget_db.get_all_category_budget_paginated(page_number,page_size)
    def update_category_budget(self, category_budget_id, category_budget: category_budget_model.CategoryBudget):
        return category_budget_db.update_category_budget(category_budget_id, category_budget)
    def delete_category_budget(self, category_budget_id):
        return category_budget_db.delete_category_budget(category_budget_id)