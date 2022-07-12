from fastapi import APIRouter ,status , File, UploadFile
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from app.service import departments_users
from typing import Union
import json
from app.models import departments_users as department_user_model

router = APIRouter()
departments_users_service = departments_users.DepartmentUsersService()

@router.post("/")
async def CreateDepartmentUser(department_user: department_user_model.CreateDepartmentUserForm):
    return await departments_users_service.CreateDepartmentUser(department_user)

@router.get("/{department_user_id}")
async def GetOneDepartmentUser(department_user_id: int):
    return await departments_users_service.GetOneDepartmentUser(department_user_id)

@router.get("/")
async def GetAllDepartmentsUsersPaginated(page_number: int, page_size: int):
    return await departments_users_service.GetAllDepartmentsUsersPaginated(page_number, page_size)

@router.put("/{department_user_id}")
async def UpdateDepartmentUser(department_user_id: int, department_user: department_user_model.CreateDepartmentUserForm):
    return await departments_users_service.UpdateDepartmentUser(department_user_id, department_user)

@router.delete("/{department_user_id}")
async def DeleteUser(department_user_id: int):
    return await departments_users_service.DeleteDepartmentUser(department_user_id)