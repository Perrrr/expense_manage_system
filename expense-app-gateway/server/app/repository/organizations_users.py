from datetime import datetime
import uuid


from pydantic import BaseModel
from typing import Optional
import uuid
import datetime
from app.repository import organizations_users_db
from app.models import organizations_users as organization_user_model




class OrganizationsUserRepository():
    def __init__(self):
        pass
    def create_organizations_users(self, organization_user: organization_user_model.OrganizationsUsers):
        return organizations_users_db.create_organizations_users(organization_user)
    def get_one_organization_user(self, organization_user_id):
        return organizations_users_db.get_one_organization_user(organization_user_id)
    def get_all_organizations_users_paginated(self, page_number, page_size):
        return organizations_users_db.get_all_organizations_users_paginated(page_number, page_size)
    def update_organizations_users(self, organization_user_id, organization_user: organization_user_model.OrganizationsUsers):
        return organizations_users_db.update_organization_user(organization_user_id, organization_user)
    def delete_organizations_users(self, organization_user_id):
        return organizations_users_db.delete_organizations_users(organization_user_id)
       
