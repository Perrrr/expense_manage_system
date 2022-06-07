from app.repository.users import UsersRepository
from app.service import users
from app.models import users as users_model

UsersRepository = UsersRepository()


async def CreateUser(user : users_model.CreateUserForm):
    return await UsersRepository.create_users(user)

async def GetOneUser(user_id):
    return await UsersRepository.get_one_user(user_id)

async def GetAllUsersPaginated(page_number, page_size):
    return await UsersRepository.get_all_users_paginated(page_number, page_size)

async def UpdateUser(user_id, user : users_model.CreateUserForm):
    return await UsersRepository.update_users(user_id, user)

async def DeleteUser(user_id):
    return await UsersRepository.delete_users(user_id)
