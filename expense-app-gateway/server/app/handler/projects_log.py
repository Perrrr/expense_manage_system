from fastapi import APIRouter ,status , File, UploadFile
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from app.service import projects_log
from typing import Union
import json
from app.models import projects_log as project_log_model

router = APIRouter()
projects_log_service = projects_log.ProjectsLogService()

@router.post("/")
async def CreateProjectLog(project_log: project_log_model.CreateProjectLogForm):
    return await projects_log_service.CreateProjectLog(project_log)

@router.get("/{project_log_id}")
async def GetOneProjectLog(project_log_id: int):
    return await projects_log_service.GetOneProjectLog(project_log_id)

@router.get("/")
async def GetAllProjectsLogPaginated(page_number: int ,page_size: int):
    return await projects_log_service.GetAllProjectsLogPaginated(page_number, page_size)

@router.put("/{project_log_id}")
async def UpdateProjectLog(project_log_id: int, project_log: project_log_model.CreateProjectLogForm):
    return await projects_log_service.UpdateProjectLog(project_log_id, project_log)

@router.delete("/{project_log_id}")
async def DeleteProjectLog(project_log_id: int):
    return await projects_log_service.DeleteProjectLog(project_log_id)

