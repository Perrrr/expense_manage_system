from datetime import datetime
import uuid


from pydantic import BaseModel
from typing import Optional
import uuid
import datetime
from app.repository import organizations_users_roles_db
from app.models import organizations_users_roles as organization_user_role_model




class OrganizationsUserRoleRepository():
    def __init__(self):
        pass
    def create_organizations_users_roles(self, organization_user_role: organization_user_role_model.OrganizationsUsersRoles):
        return organizations_users_roles_db.create_organizations_users_roles(organization_user_role)
    def get_one_organization_user_role(self, organization_user_role_id):
        return organizations_users_roles_db.get_one_organization_user_role(organization_user_role_id)
    def get_all_organizations_users_roles_paginated(self, page_number, page_size):
        return organizations_users_roles_db.get_all_organizations_users_roles_paginated(page_number, page_size)
    def update_organizations_users_roles(self, organization_user_role_id, organization_user_role: organization_user_role_model.OrganizationsUsersRoles):
        return organizations_users_roles_db.update_organization_user_role(organization_user_role_id, organization_user_role)
    def delete_organizations_users_roles(self, organization_user_role_id):
        return organizations_users_roles_db.delete_organizations_users_roles(organization_user_role_id)
    
