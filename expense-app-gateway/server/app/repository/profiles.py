from datetime import datetime
import profile
from pyexpat import model
import uuid


from pydantic import BaseModel
from typing import Optional
import uuid
import datetime
from app.repository import profiles_db
from app.models import profiles as profile_model




class ProfileRepository():
    def __init__(self):
        pass
    def create_profiles(self, profile: profile_model.Profiles):
        return profiles_db.create_profiles(profile)
    def get_one_profile(self,profile_id):
        return profiles_db.get_one_profile(profile_id)
    def get_profile_by_user_id(self, user_id):
        return profiles_db.get_profile_by_user_id(user_id)
    def get_all_profiles_paginated(self, page_number, page_size):
        return profiles_db.get_all_profiles_paginated(page_number,page_size)
    def update_profiles(self, profile_id, profile: profile_model.Profiles):
        return profiles_db.update_profiles(profile_id,profile)
    def delete_profiles(self, profile_id):
        return profiles_db.delete_profiles(profile_id)
    