from fastapi import APIRouter ,status , File, UploadFile
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from app.service import departments
from typing import Union
import json
from app.models import departments as department_model

router = APIRouter()
department_service = departments.DepartmentsService()

@router.post("/")
async def CreateDepartment(department: department_model.CreateDepartmentForm):
    return await department_service.CreateDepartment(department)

@router.get("/{department_id}")
async def GetOneDepartment(department_id: int):
    return await department_service.GetOneDepartment(department_id)

@router.get("/")
async def GetAllDepartmentsPaginated(page_number: int, page_size: int):
    return await department_service.GetAllDepartmentsPaginated(page_number, page_size)

@router.put("/{department_id}")
async def UpdateDepartment(department_id: int, department: department_model.CreateDepartmentForm):
    return await department_service.UpdateDepartment(department_id, department)

@router.delete("/{department_id}")
async def DeleteDepartment(department_id: int):
    return await department_service.DeleteDepartment(department_id)
    