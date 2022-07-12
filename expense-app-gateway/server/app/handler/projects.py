from fastapi import APIRouter ,status , File, UploadFile
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from app.service import projects
from typing import Union
import json
from app.models import projects as project_model

router = APIRouter()
projects_service = projects.ProjectsService()

@router.post("/")
async def CreateProject(project : project_model.CreateProjectForm):
    return await projects_service.CreateProject(project)

@router.get("/{project_id}")
async def GetOneProject(project_id: int):
    return await projects_service.GetOneProject(project_id)

@router.get("/")
async def GetAllProjectsPaginated(page_number: int, page_size: int):
    return await projects_service.GetAllProjectsPaginated(page_number, page_size)

@router.put("/{project_id}")
async def UpdateProject(project_id: int, project: project_model.CreateProjectForm):
    return await projects_service.UpdateProject(project_id, project)

@router.delete("/{project_id}")
async def DeleteProject(project_id: int):
    return await projects_service.DeleteProject(project_id)

