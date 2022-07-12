from app.repository.profiles import ProfileRepository
from app.service import profiles
from app.models import profiles as profiles_model

ProfileRepository = ProfileRepository()

async def CreateProfile(profile: profiles_model.CreateProfileForm):
    return await ProfileRepository.create_profiles(profile)

async def GetOneProfile(profile_id):
    return await ProfileRepository.get_one_profile(profile_id)

async def GetAllProfilesPaginated(page_number, page_size):
    return await ProfileRepository.get_all_profiles_paginated(page_number, page_size)

async def UpdateProfile(profile_id, profile: profiles_model.CreateProfileForm):
    return await ProfileRepository.update_profiles(profile_id, profile)

async def DeleteProfile(profile_id):
    return await ProfileRepository.delete_profiles(profile_id)