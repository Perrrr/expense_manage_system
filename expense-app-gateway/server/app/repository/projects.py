from datetime import datetime
from pyexpat import model
import uuid


from pydantic import BaseModel
from typing import Optional
import uuid
import datetime
from app.repository import projects_db
from app.models import projects as project_model




class ProjectsRepository():
    def __init__(self):
        pass
    def create_projects(self, project: project_model.Projects):
        return projects_db.create_projects(project)
    def get_one_project(self, project_id):
        return projects_db.get_one_project(project_id)
    def get_all_projects_paginated(self, page_number, page_size):
        return projects_db.get_all_projects_paginated(page_number, page_size)
    def update_projects(self, project_id, project: project_model.Projects):
        return projects_db.update_projects(project_id, project)
    def delete_projects(self, project_id):
        return projects_db.delete_projects(project_id)
    