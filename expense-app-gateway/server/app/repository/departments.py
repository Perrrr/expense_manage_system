from datetime import datetime
import profile
from pyexpat import model
import uuid


from pydantic import BaseModel
from typing import Optional
import uuid
import datetime
from app.repository import departments_db
from app.models import departments as department_model




class DepartmentsRepository():
    def __init__(self):
        pass
    def create_departments(self, department: department_model.Departments):
        return departments_db.create_departments(department)
    def get_one_department(self, department_id):
        return departments_db.get_one_department(department_id)
    def get_all_departments_paginated(self, page_number, page_size):
        return departments_db.get_all_departments_paginated(page_number, page_size)
    def update_departments(self, department_id, department: department_model.Departments):
        return departments_db.update_departments(department_id, department)
    def delete_departments(self, department_id):
        return departments_db.delete_departments(department_id)
    