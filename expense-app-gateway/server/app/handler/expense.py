from fastapi import APIRouter ,status , File, UploadFile
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from app.service import expense
from typing import Union
import json
from app.models import expense as expense_model

router = APIRouter()
expenses_service = expense.ExpenseService()

@router.post("/")
async def CreateExpense(expense: expense_model.CreateExpenseForm):
    return await expenses_service.CreateExpense(expense)

@router.get("/{expense_id}")
async def GetOneExpense(expense_id: int):
    return await expenses_service.GetOneExpense(expense_id)

@router.get("/")
async def GetAllExpensePaginated(page_number: int, page_size: int):
    return await expenses_service.GetAllExpensesPaginated(page_number, page_size)

@router.put("/{expense_id}")
async def UpdateExpense(expense_id: int, expense: expense_model.CreateExpenseForm):
    return await expenses_service.UpdateExpense(expense_id, expense)

@router.delete("/{expense_id}")
async def DeleteExpense(expense_id: int):
    return await expenses_service.DeleteExpense(expense_id)
    