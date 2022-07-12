from datetime import datetime
import uuid


from pydantic import BaseModel
from typing import Optional
import uuid
import datetime
from app.repository import roles_db
from app.models import roles as role_model




class RolesRepository():
    def __init__(self):
        pass
    def create_roles(self, role: role_model.Roles):
        return roles_db.create_roles(role)
    def get_one_role(self, role_id):
        return roles_db.get_one_role(role_id)
    def get_all_roles_paginated(self, page_number, page_size):
        return roles_db.get_all_roles_paginated(page_number, page_size)
    def update_roles(self, role_id, role: role_model.Roles):
        return roles_db.update_roles(role_id, role)
    def delete_roles(self, role_id):
        return roles_db.delete_roles(role_id)
       
