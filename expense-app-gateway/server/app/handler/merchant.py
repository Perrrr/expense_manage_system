from fastapi import APIRouter ,status , File, UploadFile
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from app.service import merchant
from typing import Union
import json
from app.models import merchant as merchant_model

router = APIRouter()
merchant_service = merchant.MerchantService()

@router.post("/")
async def CreateMerchant(merchant: merchant_model.CreateMerchantForm):
    return await merchant_service.CreateMerchant(merchant)

@router.get("/{merchant_id}")
async def GetOneMerchant(merchant_id: int):
    return await merchant_service.GetOneMerchant(merchant_id)

@router.get("/")
async def GetAllMerchantPaginated(page_number: int, page_size: int):
    return await merchant_service.GetAllMerchantPaginated(page_number, page_size)

@router.put("/{merchant_id}")
async def UpdateMerchant(merchant_id: int, merchant: merchant_model.CreateMerchantForm):
    return await merchant_service.UpdateMerchant(merchant_id, merchant)

@router.delete("/{merchant_id}")
async def DeleteMerchant(merchant_id: int):
    return await merchant_service.DeleteMerchant(merchant_id)