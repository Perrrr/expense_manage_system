from app.repository import user_budget_db
from app.models import user_budget as user_budget_model

class UserBudgetRepository():
    def __init__(self):
        pass
    def create_user_budget(self, user_budget: user_budget_model.UserBudget):
        return user_budget_db.create_user_budget(user_budget)
    def get_one_user_budget(self, user_budget_id):
        return user_budget_db.get_one_user_budget(user_budget_id)
    def get_all_user_budget_paginated(self, page_number, page_size):
        return user_budget_db.get_all_user_budget_paginated(page_number,page_size)
    def update_user_budget(self, user_budget_id, user_budget: user_budget_model.UserBudget):
        return user_budget_db.update_user_budget(user_budget_id, user_budget)
    def delete_user_budget(self, user_budget_id):
        return user_budget_db.delete_user_budget(user_budget_id)