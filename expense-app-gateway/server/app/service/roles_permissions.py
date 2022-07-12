from app.service import roles_permissions_service
from app.models import roles_permissions as role_permission_model

class RolesPermissionsService():
    def __init__(self):
        pass
    def CreateRolePermission(self, role_permission: role_permission_model.CreateRolePermissionForm):
        return roles_permissions_service.CreateRolePermission(role_permission)
    def GetOneRolePermission(self, role_permission_id):
        return roles_permissions_service.GetOneRolePermission(role_permission_id)
    def GetAllRolesPermissionsPaginated(self, page_number, page_size):
        return roles_permissions_service.GetAllRolesPermissionsPaginated(page_number, page_size)
    def UpdateRolePermission(self, role_permission_id,role_permission: role_permission_model.CreateRolePermissionForm):
        return roles_permissions_service.UpdateRolePermission(role_permission_id, role_permission)
    def DeleteRolePermission(self, role_permission_id):
        return roles_permissions_service.DeleteRolePermission(role_permission_id)