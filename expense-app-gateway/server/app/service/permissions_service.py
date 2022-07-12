from app.repository.permissions import PermissionsRepository
from app.models import  permissions as permission_model

PermissionsRepository = PermissionsRepository()

async def CreatePermission(permission: permission_model.CreatePermissionForm):
    return await PermissionsRepository.create_permissions(permission)

async def GetOnePermission(permission_id):
    return await PermissionsRepository.get_one_permission(permission_id)

async def GetAllPermissionsPaginated(page_number, page_size):
    return await PermissionsRepository.get_all_permissions_paginated(page_number, page_size)

async def UpdatePermission(permission_id, permission:permission_model.CreatePermissionForm):
    return await PermissionsRepository.update_permissions(permission_id, permission)

async def DeletePermission(permission_id):
    return await PermissionsRepository.delete_permissions(permission_id)