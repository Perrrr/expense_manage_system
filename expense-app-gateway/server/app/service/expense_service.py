from app.repository.expense import ExpenseRepository
from app.models import expense as expense_model

ExpenseRepository = ExpenseRepository()

async def CreateExpense(expense: expense_model.CreateExpenseForm):
    return await ExpenseRepository.create_expense(expense)

async def GetOneExpense(expense_id):
    return await ExpenseRepository.get_one_expense(expense_id)

async def GetAllExpensesPaginated(page_number, page_size):
    return await ExpenseRepository.get_all_expense_paginated(page_number, page_size)

async def UpdateExpense(expense_id, expense: expense_model.CreateExpenseForm):
    return await ExpenseRepository.update_expense(expense_id,expense)

async def DeleteExpense(expense_id):
    return await ExpenseRepository.delete_expense(expense_id)
