from app.repository.departments_users import DepartmentsUsersRepository
from app.models import departments_users as department_user_model

DepartmentsUsersRepository = DepartmentsUsersRepository()

async def CreateDepartmentUser(department_user: department_user_model.CreateDepartmentUserForm):
    return await DepartmentsUsersRepository.create_departments_users(department_user)

async def GetOneDepartmentUser(department_user_id):
    return await DepartmentsUsersRepository.get_one_department_user(department_user_id)

async def GetAllDepartmentsUsersPaginated(page_number, page_size):
    return await DepartmentsUsersRepository.get_all_departments_users_paginated(page_number, page_size)

async def UpdateDepartmentUser(department_user_id, department_user: department_user_model.CreateDepartmentUserForm):
    return await DepartmentsUsersRepository.update_departments_users(department_user_id, department_user)

async def DeleteDepartmentUser(department_user_id):
    return await DepartmentsUsersRepository.delete_departments_users(department_user_id)