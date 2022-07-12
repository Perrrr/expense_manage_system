from app.repository.projects import ProjectsRepository
from app.models import projects as project_model

ProjectsRepository = ProjectsRepository()

async def CreateProject(project: project_model.CreateProjectForm):
    return await ProjectsRepository.create_projects(project)

async def GetOneProject(project_id):
    return await ProjectsRepository.get_one_project(project_id)

async def GetAllProjectsPaginated(page_number, page_size):
    return await ProjectsRepository.get_all_projects_paginated(page_number, page_size)

async def UpdateProject(project_id, project: project_model.CreateProjectForm):
    return await ProjectsRepository.update_projects(project_id, project)

async def DeleteProject(project_id):
    return await ProjectsRepository.delete_projects(project_id)