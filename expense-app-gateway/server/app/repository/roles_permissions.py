from datetime import datetime
import uuid


from pydantic import BaseModel
from typing import Optional
import uuid
import datetime
from app.repository import roles_permissions_db
from app.models import roles_permissions as role_permission_model




class RolesPermissionsRepository():
    def __init__(self):
        pass
    def create_roles_permissions(self, role_permission: role_permission_model.RolesPermissions):
        return roles_permissions_db.create_roles_permissions(role_permission)
    def get_one_role_permission(self, role_permission_id):
        return roles_permissions_db.get_one_role_permission(role_permission_id)
    def get_all_roles_permissions_paginated(self, page_number, page_size):
        return roles_permissions_db.get_all_roles_permissions_paginated(page_number, page_size)
    def update_roles_permissions(self, role_permission_id, role_permission: role_permission_model.RolesPermissions):
        return roles_permissions_db.update_roles_permissions(role_permission_id, role_permission)
    def delete_roles_permissions(self, role_permission_id):
        return roles_permissions_db.delete_roles_permissions(role_permission_id)
       
