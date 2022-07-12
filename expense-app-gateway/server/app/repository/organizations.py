from datetime import datetime
import uuid


from pydantic import BaseModel
from typing import Optional
import uuid
import datetime
from app.repository import organizations_db
from app.models import organizations as organization_model




class OrganizationsRepository():
    def __init__(self):
        pass
    def create_organizations(self, organization: organization_model.Organizations):
        return organizations_db.create_organizations(organization)
    def get_one_organization(self, organization_id):
        return organizations_db.get_one_organization(organization_id)
    def get_all_organizations_paginated(self, page_number, page_size):
        return organizations_db.get_all_organizations_paginated(page_number, page_size)
    def update_organizations(self, organization_id, organization: organization_model.Organizations):
        return organizations_db.update_organizations(organization_id, organization)
    def delete_organizations(self, organization_id):
        return organizations_db.delete_organizations(organization_id)
       
    