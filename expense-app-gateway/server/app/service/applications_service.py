from app.repository.applications import ApplicationsRepository
from app.service import applications
from app.models import applications as applications_model

ApplicationsRepository = ApplicationsRepository()

async def CreateApplication(application: applications_model.CreateApplicationForm):
    return await ApplicationsRepository.create_applications(application)

async def GetOneApplication(application_id):
    return await ApplicationsRepository.get_one_application(application_id)

async def GetAllapplicationsPaginated(page_number, page_size):
    return await ApplicationsRepository.get_all_applications_paginated(page_number, page_size)

async def UpdateApplication(application_id, application: applications_model.CreateApplicationForm):
    return await ApplicationsRepository.update_applications(application_id, application)

async def DeleteApplication(application_id):
    return await ApplicationsRepository.delete_applications(application_id)