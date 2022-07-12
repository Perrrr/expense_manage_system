from datetime import datetime
from pyexpat import model
import uuid


from pydantic import BaseModel
from typing import Optional
import uuid
import datetime
from app.repository import projects_log_db
from app.models import projects_log as project_log_model




class ProjectsLogRepository():
    def __init__(self):
        pass
    def create_projects_log(self, project_log: project_log_model.ProjectsLog):
        return projects_log_db.create_projects_log(project_log)
    def get_one_project_log(self, project_log_id):
        return projects_log_db.get_one_project_log(project_log_id)
    def get_all_projects_log_paginated(self, page_number, page_size):
        return projects_log_db.get_all_projects_log_paginated(page_number,page_size)
    def update_projects_log(self, project_log_id, project_log: project_log_model.ProjectsLog):
        return projects_log_db.update_projects_log(project_log_id, project_log)
    def delete_projects_log(self, project_log_id):
        return projects_log_db.delete_projects_log(project_log_id)
    