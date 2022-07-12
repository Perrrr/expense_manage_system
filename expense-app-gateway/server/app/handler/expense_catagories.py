from fastapi import APIRouter ,status , File, UploadFile
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from app.service import expense_catagories
from typing import Union
import json
from app.models import expense_catagories as expense_catagorie_model

router = APIRouter()
expense_catagories_service = expense_catagories.ExpenseCatagoriesService()

@router.post("/")
async def CreateExpenseCatagorie(expense_catagorie: expense_catagorie_model.CreateExpenseCatagoriesForm):
    return await expense_catagories_service.CreateExpenseCaragorie(expense_catagorie)

@router.get("/{expense_catagorie_id}")
async def GetOneExpenseCatagorie(expense_catagorie_id: int):
    return await expense_catagories_service.GetOneExpenseCaragorie(expense_catagorie_id)

@router.get("/")
async def GetAllExpenseCatagoriesPaginated(page_number: int, page_size: int):
    return await expense_catagories_service.GetAllExpenseCaragoriesPaginated(page_number, page_size)

@router.put("/{expense_catagorie_id}")
async def UpdateExpenseCatagorie(expense_catagorie_id: int, expense_catagorie: expense_catagorie_model.CreateExpenseCatagoriesForm):
    return await expense_catagories_service.UpdateExpenseCaragorie(expense_catagorie_id, expense_catagorie)

@router.delete("/{expense_catagorie_id}")
async def DeleteExpenseCatagorie(expense_catagorie_id: int):
    return await expense_catagories_service.DeleteExpenseCaragorie(expense_catagorie_id)
    