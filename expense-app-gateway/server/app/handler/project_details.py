from fastapi import APIRouter ,status , File, UploadFile
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from app.service import project_details
from typing import Union
import json
from app.models import project_details as project_detail_model

router = APIRouter()
project_details_service = project_details.ProjectDetailsService()

@router.post("/")
async def CreateProjectDetail(project_detail: project_detail_model.CreateProjectDetailForm):
    return await project_details_service.CreateProjectDetail(project_detail)

@router.get("/{project_detail_id}")
async def GetOneProjectDetail(project_detail_id: int):
    return await project_details_service.GetOneProjectDetail(project_detail_id)

@router.get("/")
async def GetAllProjectDetailsPaginated(page_number: int , page_size: int):
    return await project_details_service.GetAllProjectDetailsPaginated(page_number, page_size)

@router.put("/{project_detail_id}")
async def UpdateProjectDetail(project_detail_id: int, project_detail: project_detail_model.CreateProjectDetailForm):
    return await project_details_service.UpdateProjectDetail(project_detail_id, project_detail)

@router.delete("/{project_detail_id}")
async def DeleteProjectDetail(project_detail_id: int):
    return await project_details_service.DeleteProjectDetail(project_detail_id)