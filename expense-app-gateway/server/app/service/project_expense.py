from app.service import project_expense_service
from app.models import project_expense as project_expense_model

class ProjectExpenseService():
    def __init__(self):
        pass
    def CreateProjectExpense(self, project_expense: project_expense_model.CreateProjectExpenseForm):
        return project_expense_service.CreateProjectExpense(project_expense)
    def GetOneProjectExpense(self, project_expense_id):
        return project_expense_service.GetOneProjectExpense(project_expense_id)
    def GetAllProjectExpensePaginated(self, page_number, page_size):
        return project_expense_service.GetAllProjectExpensePaginated(page_number, page_size)
    def UpdateProjectExpense(self, project_expense_id, project_expense: project_expense_model.CreateProjectExpenseForm):
        return project_expense_service.UpdateProjectExpense(project_expense_id, project_expense)
    def DeleteProjectExpense(self, project_expense_id):
        return project_expense_service.DeleteProjectExpense(project_expense_id)
    