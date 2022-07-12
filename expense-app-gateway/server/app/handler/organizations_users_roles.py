from fastapi import APIRouter ,status , File, UploadFile
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from app.service import organizations_users_roles
from typing import Union
import json
from app.models import organizations_users_roles as organization_user_role_model

router = APIRouter()
organizations_users_roles_service = organizations_users_roles.OrganizationUserRoleService()

@router.post("/")
async def CreateOrganizationUserRole(organization_user_role: organization_user_role_model.CreateOrganizationUserRoleForm):
    return await organizations_users_roles_service.CreateOrganizationUserRole(organization_user_role)

@router.get("/{organization_user_role_id}")
async def GetOneOrganizationUserRole(organization_user_role_id: int):
    return await organizations_users_roles_service.GetOneOrganizationUserRole(organization_user_role_id)

@router.get("/")
async def GetAllOrganizationsUsersRolesPaginated(page_number: int, page_size:int):
    return await organizations_users_roles_service.GetAllOrganizationsUsersRolesPaginated(page_number, page_size)

@router.put("/{organization_user_role_id}")
async def UpdateOrganizationUserRole(organization_user_role_id: int, organization_user_role: organization_user_role_model.CreateOrganizationUserRoleForm):
    return await organizations_users_roles_service.UpdateOrganizationUserRole(organization_user_role_id, organization_user_role)

@router.delete("/{organization_user_role_id}")
async def DeleteOrganizationUserRole(organization_user_role_id: int):
    return await organizations_users_roles_service.DeleteOrganizationUserRole(organization_user_role_id)