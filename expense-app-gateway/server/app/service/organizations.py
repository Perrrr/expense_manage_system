from datetime import datetime
import uuid

from pydantic import BaseModel
from typing import Optional
import uuid
import datetime
from app.service import organizations_service
from app.models import organizations as organization_model

class OrganizationService():
    def __init__(self):
        pass
    def CreateOrganization(self, organization: organization_model.CreateOrganizationForm):
        return organizations_service.CreateOrganization(organization)
    def GetOneOrganization(self, organization_id):
        return organizations_service.GetOneOrganization(organization_id)
    def GetAllOrganizationsPaginated(self, page_number, page_size):
        return organizations_service.GetAllOrganizationsPaginated(page_number, page_size)
    def UpdateOrganization(self, organization_id,organization: organization_model.CreateOrganizationForm):
        return organizations_service.UpdateOrganization(organization_id,organization)
    def DeleteOrganization(self, organization_id):
        return organizations_service.DeleteOrganization(organization_id)