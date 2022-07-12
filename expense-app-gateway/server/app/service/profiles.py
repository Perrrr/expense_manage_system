from cProfile import Profile
from datetime import datetime
import uuid

from pydantic import BaseModel
from typing import Optional
import uuid
import datetime
from app.service import profiles_service
from app.models import profiles as profile_model


class ProfileService():
    def __init__(self) :
        pass
    def CreateProfile(self, profile: profile_model.CreateProfileForm):
        return profiles_service.CreateProfile(profile)
    def GetOneProfile(self, profile_id):
        return profiles_service.GetOneProfile(profile_id)
    def GetAllProfilesPaginated(self, page_number, page_size): 
        return profiles_service.GetAllProfilesPaginated(page_number, page_size)
    def UpdateProfile(self, profile_id, profile: profile_model.CreateProfileForm):
        return profiles_service.UpdateProfile(profile_id, profile)
    def DeleteProfile(self, profile_id):
        return profiles_service.DeleteProfile(profile_id)