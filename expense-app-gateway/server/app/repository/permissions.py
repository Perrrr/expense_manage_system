from datetime import datetime
import uuid


from pydantic import BaseModel
from typing import Optional
import uuid
import datetime
from app.repository import permissions_db
from app.models import permissions as permission_model




class PermissionsRepository():
    def __init__(self):
        pass
    def create_permissions(self, permission: permission_model.Permissions):
        return permissions_db.create_permissions(permission)
    def get_one_permission(self, permission_id):
        return permissions_db.get_one_permission(permission_id)
    def get_all_permissions_paginated(self, page_number, page_size):
        return permissions_db.get_all_permissions_paginated(page_number, page_size)
    def update_permissions(self, permission_id, permission: permission_model.Permissions):
        return permissions_db.update_permissions(permission_id, permission)
    def delete_permissions(self, permission_id):
        return permissions_db.delete_permissions(permission_id)
       
