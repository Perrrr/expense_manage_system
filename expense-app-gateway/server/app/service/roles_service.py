from app.repository.roles import RolesRepository
from app.models import roles as role_model

RolesRepository = RolesRepository()

async def CreateRole(role: role_model.CreateRoleForm):
    return await RolesRepository.create_roles(role)

async def GetOneRole(role_id):
    return await RolesRepository.get_one_role(role_id)

async def GetAllRolesPaginated(page_number, page_size):
    return await RolesRepository.get_all_roles_paginated(page_number, page_size)

async def UpdateRole(role_id,role: role_model.CreateRoleForm):
    return await RolesRepository.update_roles(role_id, role)

async def DeleteRole(role_id):
    return await RolesRepository.delete_roles(role_id)