from datetime import datetime
import profile
from pyexpat import model
import uuid


from pydantic import BaseModel
from typing import Optional
import uuid
import datetime
from app.repository import departments_users_db
from app.models import departments_users as department_user_model




class DepartmentsUsersRepository():
    def __init__(self):
        pass
    def create_departments_users(self, department_user: department_user_model.DepartmentsUsers):
        return departments_users_db.create_departments_users(department_user)
    def get_one_department_user(self, department_user_id):
        return departments_users_db.get_one_department_user(department_user_id)
    def get_all_departments_users_paginated(self, page_number, page_size):
        return departments_users_db.get_all_departments_users_paginated(page_number, page_size)
    def update_departments_users(self, department_user_id, department_user: department_user_model.DepartmentsUsers):
        return departments_users_db.update_departments_users(department_user_id, department_user)
    def delete_departments_users(self, department_user_id):
        return departments_users_db.delete_departments_users(department_user_id)
    