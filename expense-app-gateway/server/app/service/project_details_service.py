from app.repository.project_details import ProjectDetailsRepository
from app.models import project_details as project_detail_model

ProjectDetailsRepository = ProjectDetailsRepository()

async def CreateProjectDetail(project_detail: project_detail_model.CreateProjectDetailForm):
    return await ProjectDetailsRepository.create_project_details(project_detail)

async def GetOneProjectDetail(project_detail_id):
    return await ProjectDetailsRepository.get_one_project_detail(project_detail_id)

async def GetAllProjectDetailsPaginated(page_number, page_size):
    return await ProjectDetailsRepository.get_all_project_details_paginated(page_number, page_size)

async def UpdateProjectDetail(project_detail_id,project_detail: project_detail_model.CreateProjectDetailForm):
    return await ProjectDetailsRepository.update_project_details(project_detail_id, project_detail)

async def DeleteProjectDetail(project_detail_id):
    return await ProjectDetailsRepository.delete_project_details(project_detail_id)