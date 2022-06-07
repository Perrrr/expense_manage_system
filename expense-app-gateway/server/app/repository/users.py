from datetime import datetime
import uuid


from pydantic import BaseModel
from typing import Optional
import uuid
import datetime
from app.repository import users_db
from app.models import users as user_model




class UsersRepository():
    def __init__(self):
        pass
    def create_users(self, user : user_model.Users):
        return users_db.create_users(user)
    def get_one_user(self, user_id):
        return users_db.get_one_user(user_id)
    def get_all_users_paginated(self, page_number, page_size):
        return users_db.get_all_users_paginated(page_number, page_size)
    def update_users(self, user_id, user : user_model.Users):
        return users_db.update_users(user_id, user)
    def delete_users(self, user_id):
        return users_db.delete_users(user_id)
       
