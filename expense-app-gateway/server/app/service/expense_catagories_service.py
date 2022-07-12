from app.repository.expense_catagories import ExpenseCatagoriesRepository
from app.models import expense_catagories as expense_catagories_model

ExpenseCatagoriesRepository = ExpenseCatagoriesRepository()

async def CreateExpenseCatagorie(expense_catagorie: expense_catagories_model.CreateExpenseCatagoriesForm):
    return await ExpenseCatagoriesRepository.create_expense_catagories(expense_catagorie)

async def GetOneExpenseCatagorie(expense_catagorie_id):
    return await ExpenseCatagoriesRepository.get_one_expense_catagorie(expense_catagorie_id)

async def GetAllExpenseCaragoriesPaginated(page_number, page_size):
    return await ExpenseCatagoriesRepository.get_all_expense_catagories_paginated(page_number, page_size)

async def UpdateExpenseCaragorie(expense_catagorie_id, expense_catagorie: expense_catagories_model.CreateExpenseCatagoriesForm):
    return await ExpenseCatagoriesRepository.update_expense_catagories(expense_catagorie_id, expense_catagorie)

async def DeleteExpenseCatagorie(expense_catagorie_id):
    return await ExpenseCatagoriesRepository.delete_expense_catagories(expense_catagorie_id)
