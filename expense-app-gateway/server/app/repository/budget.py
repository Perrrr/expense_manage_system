from app.repository import budget_db
from app.models import budget as budget_model

class BudgetRepository():
    def __init__(self):
        pass
    def create_budget(self, budget: budget_model.Budget):
        return budget_db.create_budget(budget)
    def get_one_budget(self, budget_id):
        return budget_db.get_one_budget(budget_id)
    def get_all_budget_paginated(self, page_number, page_size):
        return budget_db.get_all_budget_paginated(page_number,page_size)
    def update_budget(self, budget_id, budget: budget_model.Budget):
        return budget_db.update_budget(budget_id, budget)
    def delete_budget(self, budget_id):
        return budget_db.delete_budget(budget_id)