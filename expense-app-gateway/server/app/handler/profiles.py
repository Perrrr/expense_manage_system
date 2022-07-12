from urllib import response
from fastapi import APIRouter ,status , File, UploadFile
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from app.service import profiles
from typing import Union
import json
from app.models import profiles as profile_model

router = APIRouter()
profile_service = profiles.ProfileService()


@router.post("/")
async def CreateProfile(profile : profile_model.CreateProfileForm):
    return await profile_service.CreateProfile(profile)

@router.get("/{profile_id}" ,  response_model=profile_model.CreateProfileForm)
async def GetOneProfile(profile_id: int):
    return await profile_service.GetOneProfile(profile_id)

@router.get("/")
async def GetAllProfilesPaginated(page_number: int, page_size: int):
    return await profile_service.GetAllProfilesPaginated(page_number, page_size)

@router.put("/{profile_id}")
async def UpdateProfile(profile_id: int, profile: profile_model.CreateProfileForm):
    return await profile_service.UpdateProfile(profile_id, profile)

@router.delete("/{profile_id}")
async def DeleteProfile(profile_id: int):
    return await profile_service.DeleteProfile(profile_id)