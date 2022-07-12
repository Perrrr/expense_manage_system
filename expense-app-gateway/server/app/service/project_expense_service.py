from app.repository.project_expense import ProjectExpenseRepository
from app.models import project_expense as project_expense_model

ProjectExpenseRepository = ProjectExpenseRepository()

async def CreateProjectExpense(project_expense: project_expense_model.CreateProjectExpenseForm):
    return await ProjectExpenseRepository.create_project_expense(project_expense)

async def GetOneProjectExpense(project_expense_id):
    return await ProjectExpenseRepository.get_one_project_expense(project_expense_id)

async def GetAllProjectExpensePaginated(page_number, page_size):
    return await ProjectExpenseRepository.get_all_project_expense_paginated(page_number, page_size)

async def UpdateProjectExpense(project_expense_id, project_expense: project_expense_model.CreateProjectExpenseForm):
    return await ProjectExpenseRepository.update_project_expense(project_expense_id, project_expense)

async def DeleteProjectExpense(project_expense_id):
    return await ProjectExpenseRepository.delete_project_expense(project_expense_id)