from fastapi import APIRouter ,status , File, UploadFile
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from app.service import roles
from typing import Union
import json
from app.models import roles as role_model

router = APIRouter()
roles_service = roles.RolesService()

@router.post("/")
async def CreateRole(role: role_model.CreateRoleForm):
    return await roles_service.CreateRole(role)

@router.get("/{role_id}")
async def GetOneRole(role_id: int):
    return await roles_service.GetOneRole(role_id)

@router.get("/")
async def GetAllRolesPaginated(page_number: int, page_size: int):
    return await roles_service.GetAllRolesPaginated(page_number, page_size)

@router.put("/{role_id}")
async def UpdateRole(role_id: int, role: role_model.CreateRoleForm):
    return await roles_service.UpdateRole(role_id, role)

@router.delete("/{role_id}")
async def DeleteRole(role_id: int):
    return await roles_service.DeleteRole(role_id)