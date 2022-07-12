from fastapi import APIRouter ,status , File, UploadFile
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from app.service import roles_permissions
from typing import Union
import json
from app.models import roles_permissions as role_permission_model

router = APIRouter()
roles_permissions_service = roles_permissions.RolesPermissionsService()

@router.post("/")
async def CreateRolePermission(role_permission: role_permission_model.CreateRolePermissionForm):
    return await roles_permissions_service.CreateRolePermission(role_permission)

@router.get("/{role_permission_id}")
async def GetOneRolePermission(role_permission_id: int):
    return await roles_permissions_service.GetOneRolePermission(role_permission_id)

@router.get("/")
async def GetAllRolesPermissions(page_number: int, page_size: int):
    return await roles_permissions_service.GetAllRolesPermissionsPaginated(page_number, page_size)

@router.put("/{role_permission_id}")
async def UpdateRolePermission(role_permission_id: int, role_permission: role_permission_model.CreateRolePermissionForm):
    return await roles_permissions_service.UpdateRolePermission(role_permission_id, role_permission)

@router.delete("/{role_permission_id}")
async def DeleteRolePermission(role_permission_id: int):
    return await roles_permissions_service.DeleteRolePermission(role_permission_id)