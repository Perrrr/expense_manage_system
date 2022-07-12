from urllib import response
from fastapi import APIRouter ,status , File, UploadFile
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from app.service import applications
from typing import Union
import json
from app.models import applications as application_model

router = APIRouter()
application_service = applications.ApplicationService()

@router.post("/")
async def CreateApplications(application: application_model.CreateApplicationForm):
    return await application_service.CreateApplication(application)

@router.get("/{application_id}")
async def GetOneApplicaton(application_id: int):
    return await application_service.GetOneApplication(application_id)

@router.get("/")
async def GetAllApplicationPaginated(page_number: int, page_size: int):
    return await application_service.GetAllApplicationsPaginated(page_number, page_size)

@router.put("/{application_id}")
async def UpdateApplication(application_id: int, application: application_model.CreateApplicationForm):
    return await application_service.UpdateApplication(application_id, application)

@router.delete("/{application_id}")
async def DeleteApplication(application_id: int):
    return await application_service.DeleteApplication(application_id)

