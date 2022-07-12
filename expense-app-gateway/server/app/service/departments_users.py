from datetime import datetime
import uuid

from pydantic import BaseModel
from typing import Optional
import uuid
import datetime
from app.service import departments_users_service
from app.models import departments_users as department_user_model


class DepartmentUsersService():
    def __init__(self):
        pass
    def CreateDepartmentUser(self, deparment_user: department_user_model.CreateDepartmentUserForm):
        return departments_users_service.CreateDepartmentUser(deparment_user)
    def GetOneDepartmentUser(self, department_user_id):
        return departments_users_service.GetOneDepartmentUser(department_user_id)
    def GetAllDepartmentsUsersPaginated(self, page_number, page_size):
        return departments_users_service.GetAllDepartmentsUsersPaginated(page_number, page_size)
    def UpdateDepartmentUser(self, department_user_id, department_user: department_user_model.CreateDepartmentUserForm):
        return departments_users_service.UpdateDepartmentUser(department_user_id, department_user)
    def DeleteDepartmentUser(self, department_user_id):
        return departments_users_service.DeleteDepartmentUser(department_user_id)

