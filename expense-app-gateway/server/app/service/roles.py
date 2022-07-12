from app.service import roles_service
from app.models import roles as role_model

class RolesService():
    def __init__(self):
        pass
    def CreateRole(self, role: role_model.CreateRoleForm):
        return roles_service.CreateRole(role)
    def GetOneRole(self, role_id):
        return roles_service.GetOneRole(role_id)
    def GetAllRolesPaginated(self, page_number, page_size):
        return roles_service.GetAllRolesPaginated(page_number, page_size)
    def UpdateRole(self, role_id, role: role_model.CreateRoleForm):
        return roles_service.UpdateRole(role_id, role)
    def DeleteRole(self, role_id):
        return roles_service.DeleteRole(role_id)