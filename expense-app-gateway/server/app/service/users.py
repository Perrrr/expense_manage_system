from datetime import datetime
import uuid

from pydantic import BaseModel
from typing import Optional
import uuid
import datetime
from app.service import users_service
from app.models import users as user_model



class UsersService():
    def __init__(self):
        pass
    def CreateUser(self, user : user_model.CreateUserForm):
        return users_service.CreateUser(user)
    def GetOneUser(self, user_id):
        return users_service.GetOneUser(user_id)
    def GetAllUsersPaginated(self, page_number, page_size):
        return users_service.GetAllUsersPaginated(page_number, page_size)
    def UpdateUser(self, user_id, user : user_model.CreateUserForm):
        return users_service.UpdateUser(user_id, user)
    def DeleteUser(self, user_id):
        return users_service.DeleteUser(user_id)
        
