from app.repository.departments import DepartmentsRepository
from app.service import departments_service
from app.models import departments as department_model

DepartmentsRepository = DepartmentsRepository()

async def CreateDepartment(department: department_model.CreateDepartmentForm):
    return await DepartmentsRepository.create_departments(department)

async def GetOneDepartment(department_id):
    return await DepartmentsRepository.get_one_department(department_id)

async def GetAllDepartmentsPaginated(page_number, page_size):
    return await DepartmentsRepository.get_all_departments_paginated(page_number, page_size)

async def UpdateDepartment(department_id, department: department_model.CreateDepartmentForm):
    return await DepartmentsRepository.update_departments(department_id, department)

async def DeleteDepartment(department_id): 
    return await DepartmentsRepository.delete_departments(department_id)