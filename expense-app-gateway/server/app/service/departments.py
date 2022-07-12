from datetime import datetime
import uuid

from pydantic import BaseModel
from typing import Optional
import uuid
import datetime
from app.service import departments_service
from app.models import departments as department_model



class DepartmentsService():
    def __init__(self):
        pass
    def CreateDepartment(self, department: department_model.CreateDepartmentForm):
        return departments_service.CreateDepartment(department)
    def GetOneDepartment(self, department_id):
        return departments_service.GetOneDepartment(department_id)
    def GetAllDepartmentsPaginated(self, page_number, page_size):
        return departments_service.GetAllDepartmentsPaginated(page_number, page_size)
    def UpdateDepartment(self, department_id, department: department_model.CreateDepartmentForm):
        return departments_service.UpdateDepartment(department_id, department)
    def DeleteDepartment(self, department_id):
        return departments_service.DeleteDepartment(department_id)
        
