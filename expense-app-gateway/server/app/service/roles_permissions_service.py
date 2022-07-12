from app.repository.roles_permissions import RolesPermissionsRepository
from app.models import roles_permissions as role_permission_model

RolesPermissionsRepository = RolesPermissionsRepository()

async def CreateRolePermission(role_permission: role_permission_model.CreateRolePermissionForm):
    return await RolesPermissionsRepository.create_roles_permissions(role_permission)

async def GetOneRolePermission(role_permission_id):
    return await RolesPermissionsRepository.get_one_role_permission(role_permission_id)

async def GetAllRolesPermissionsPaginated(page_number, page_size):
    return await RolesPermissionsRepository.get_all_roles_permissions_paginated(page_number, page_size)

async def UpdateRolePermission(role_permission_id, role_permission: role_permission_model.CreateRolePermissionForm):
    return await RolesPermissionsRepository.update_roles_permissions(role_permission_id, role_permission)

async def DeleteRolePermission(role_permission_id):
    return await RolesPermissionsRepository.delete_roles_permissions(role_permission_id)