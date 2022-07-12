from datetime import datetime
import uuid

from pydantic import BaseModel
import uuid
import datetime
from app.service import permissions_service
from app.models import permissions as permission_model

class PermissionsService():
    def __init__(self):
        pass
    def CreatePermission(self, permission: permission_model.CreatePermissionForm):
        return permissions_service.CreatePermission(permission)
    def GetOnePermission(self, permission_id):
        return permissions_service.GetOnePermission(permission_id)
    def GetAllPermissionsPaginated(self, page_number, page_size):
        return permissions_service.GetAllPermissionsPaginated(page_number, page_size)
    def UpdatePermission(self, permission_id,permission: permission_model.CreatePermissionForm):
        return permissions_service.UpdatePermission(permission_id, permission)
    def DeletePermission(self, permission_id):
        return permissions_service.DeletePermission(permission_id)