
from fastapi import APIRouter ,status , File, UploadFile
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from app.service import currencies
from typing import Union
import json
from app.models import currencies as currencie_model

router = APIRouter()
currencie_service = currencies.CurrenciesService()

@router.post("/")
async def CreateCurrencie(currencie: currencie_model.CreateCurrencieForm):
    return await currencie_service.CreateCurrencie(currencie)

@router.get("/{currencie_id}")
async def GetOneCurrencie(currencie_id: int):
    return await currencie_service.GetOneCurrencie(currencie_id)

@router.get("/")
async def GetAllCurrenciesPaginated(page_number: int, page_size: int):
    return await currencie_service.GetAllCurrenciesPaginated(page_number, page_size)

@router.put("/{currencie_id}")
async def UpdateCurrencie(currencie_id: int, currencie: currencie_model.CreateCurrencieForm):
    return await currencie_service.UpdateCurrencie(currencie_id, currencie)

@router.delete("/{currencie_id}")
async def DeleteCurrencie(currencie_id: int):
    return await currencie_service.DeleteCurrencie(currencie_id)
    