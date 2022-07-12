from fastapi import APIRouter ,status , File, UploadFile
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from app.service import permissions
from typing import Union
import json
from app.models import permissions as permission_model

router = APIRouter()
permissions_service = permissions.PermissionsService()

@router.post("/")
async def CreatePermission(permission : permission_model.CreatePermissionForm):
    return await permissions_service.CreatePermission(permission)

@router.get("/{permission_id}")
async def GetOnePermission(permission_id: int):
    return await permissions_service.GetOnePermission(permission_id)

@router.get("/")
async def GetAllPermissionsPaginated(page_number: int, page_size: int):
    return await permissions_service.GetAllPermissionsPaginated(page_number, page_size)

@router.put("/{permission_id}")
async def UpdatePermission(permission_id: int, permission: permission_model.CreatePermissionForm):
    return await permissions_service.UpdatePermission(permission_id, permission)

@router.delete("/{permission_id}")
async def DeletePermission(permission_id: int):
    return await permissions_service.DeletePermission(permission_id)