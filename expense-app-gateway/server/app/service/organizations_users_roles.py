from datetime import datetime
import uuid

from pydantic import BaseModel
from typing import Optional
import uuid
import datetime
from app.service import organizations_users_roles_service
from app.models import organizations_users_roles as organization_user_role_model

class OrganizationUserRoleService():
    def __init__(self):
        pass
    def CreateOrganizationUserRole(self, organization_user_role: organization_user_role_model.CreateOrganizationUserRoleForm):
        return organizations_users_roles_service.CreateOrganizationUserRole(organization_user_role)
    def GetOneOrganizationUserRole(self, organization_user_role_id):
        return organizations_users_roles_service.GetOneOrganizationUserRole(organization_user_role_id)
    def GetAllOrganizationsUsersRolesPaginated(self, page_number, page_size):
        return organizations_users_roles_service.GetAllOrganizationsUsersRolesPaginated(page_number, page_size)
    def UpdateOrganizationUserRole(self, organization_user_role_id, organization_user_role: organization_user_role_model.CreateOrganizationUserRoleForm):
        return organizations_users_roles_service.UpdateOrganizationUserRole(organization_user_role_id, organization_user_role)
    def DeleteOrganizationUserRole(self, organization_user_role_id):
        return organizations_users_roles_service.DeleteOrganizationUserRole(organization_user_role_id)