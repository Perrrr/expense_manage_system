from app.repository.projects_log import ProjectsLogRepository
from app.models import projects_log as project_log_model

ProjectsLogRepository = ProjectsLogRepository()

async def CreateProjectLog(project_log: project_log_model.CreateProjectLogForm):
    return await ProjectsLogRepository.create_projects_log(project_log)

async def GetOneProjectLog(project_log_id):
    return await ProjectsLogRepository.get_one_project_log(project_log_id)

async def GetAllProjectsLogPaginated(page_number, page_size):
    return await ProjectsLogRepository.get_all_projects_log_paginated(page_number, page_size)

async def UpdateProjectLog(project_log_id, project_log: project_log_model.CreateProjectLogForm):
    return await ProjectsLogRepository.update_projects_log(project_log_id, project_log)

async def DeleteProjectLog(project_log_id):
    return await ProjectsLogRepository.delete_projects_log(project_log_id)