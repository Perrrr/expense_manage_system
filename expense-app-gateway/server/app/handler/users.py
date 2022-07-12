from fastapi import APIRouter ,status , File, UploadFile
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from app.service import users
from typing import Union
import json
from app.models import users as user_model

router = APIRouter()
users_service = users.UsersService()


@router.post("/")
async def CreateUser(user: user_model.CreateUserForm):
    return await users_service.CreateUser(user)

@router.get("/{user_id}")
async def GetOneUser(user_id: int):
    return await users_service.GetOneUser(user_id)

@router.get("/")
async def GetAllUsersPaginated(page_number: int, page_size: int):
    return await users_service.GetAllUsersPaginated(page_number, page_size)

@router.put("/{user_id}")
async def UpdateUser(user_id: int, user: user_model.CreateUserForm):
    return await users_service.UpdateUser(user_id, user)

@router.delete("/{user_id}")
async def DeleteUser(user_id: int):
    return await users_service.DeleteUser(user_id)
    