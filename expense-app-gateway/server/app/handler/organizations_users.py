from fastapi import APIRouter ,status , File, UploadFile
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from app.service import organizations_users
from typing import Union
import json
from app.models import organizations_users as organization_user_model

router = APIRouter()
organizations_users_service = organizations_users.OrganizationUserservice()

@router.post("/")
async def CreateOrganizationUser(organization_user: organization_user_model.CreateOrganizationUserForm):
    return await organizations_users_service.CreateOrganizationUser(organization_user)

@router.get("/{organization_user_id}")
async def GetOneOrganizationUser(organization_user_id: int):
    return await organizations_users_service.GetOneOrganizationUser(organization_user_id)

@router.get("/")
async def GetAllOrganizationsUsersPaginated(page_number: int, page_size: int):
    return await organizations_users_service.GetAllOrganizationsUsersPaginated(page_number, page_size)

@router.put("/{organization_user_id}")
async def UpdateOrganizationUser(organization_user_id: int,organization_user: organization_user_model.CreateOrganizationUserForm):
    return await organizations_users_service.UpdateOrganizationUser(organization_user_id, organization_user)

@router.delete("/{organization_user_id}")
async def DeleteOrganizationUser(organization_user_id: int):
    return await organizations_users_service.DeleteOrganizationUser(organization_user_id)