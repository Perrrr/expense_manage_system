from fastapi import APIRouter ,status , File, UploadFile
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from app.service import organizations
from typing import Union
import json
from app.models import organizations as organization_model

router = APIRouter()
organizations_service = organizations.OrganizationService()

@router.post("/")
async def CreateOrganization(organization: organization_model.CreateOrganizationForm):
    return await organizations_service.CreateOrganization(organization)

@router.get("/{organization_id}")
async def GetOneOrganization(organization_id: int):
    return await organizations_service.GetOneOrganization(organization_id)

@router.get("/")
async def GetAllOrganizationsPaginated(page_number: int, page_size:int):
    return await organizations_service.GetAllOrganizationsPaginated(page_number, page_size)

@router.put("/{organization_id}")
async def UpdateOrganization(organization_id: int, organization: organization_model.CreateOrganizationForm):
    return await organizations_service.UpdateOrganization(organization_id, organization)

@router.delete("/{organization_id}")
async def DeleteOrganization(organization_id: int):
    return await organizations_service.DeleteOrganization(organization_id)