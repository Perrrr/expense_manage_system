from datetime import datetime
import uuid

from pydantic import BaseModel
from typing import Optional
import uuid
import datetime
from app.service import organizations_users_service
from app.models import organizations_users as organization_user_model

class OrganizationUserservice():
    def __init__(self):
        pass
    def CreateOrganizationUser(self, organization_user: organization_user_model.CreateOrganizationUserForm):
        return organizations_users_service.CreateOrganizationUser(organization_user)
    def GetOneOrganizationUser(self, organization_user_id):
        return organizations_users_service.GetOneOrganizationUser(organization_user_id)
    def GetAllOrganizationsUsersPaginated(self, page_number, page_size):
        return organizations_users_service.GetAllOrganizationsUsersPaginated(page_number, page_size)
    def UpdateOrganizationUser(self, organization_user_id,organization_user: organization_user_model.CreateOrganizationUserForm):
        return organizations_users_service.UpdateOrganizationUser(organization_user_id, organization_user)
    def DeleteOrganizationUser(self, organization_user_id):
        return organizations_users_service.DeleteOrganizationUser(organization_user_id)