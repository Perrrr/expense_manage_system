from datetime import datetime
from pyexpat import model
import uuid


from pydantic import BaseModel
from typing import Optional
import uuid
import datetime
from app.repository import project_details_db
from app.models import project_details as project_detail_model




class ProjectDetailsRepository():
    def __init__(self):
        pass
    def create_project_details(self, project_detail: project_detail_model.ProjectDetails):
        return project_details_db.create_project_details(project_detail)
    def get_one_project_detail(self,project_detail_id):
        return project_details_db.get_one_project_detail(project_detail_id)
    def get_all_project_details_paginated(self, page_number, page_size):
        return project_details_db.get_all_project_detail_paginated(page_number, page_size)
    def update_project_details(self, project_detail_id, project_detail: project_detail_model.ProjectDetails):
        return project_details_db.update_project_detail(project_detail_id, project_detail)
    def delete_project_details(self, project_detail_id):
        return project_details_db.delete_project_detail(project_detail_id)
    