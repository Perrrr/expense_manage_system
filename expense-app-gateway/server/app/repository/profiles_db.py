from cgi import print_form
from enum import unique
import json
import re
from venv import create
from app.config.database import create_connection
from datetime import date, datetime
import uuid
import asyncpg.exceptions as pg_exceptions
from app.errs.err import err_response
from app.models import profiles as profile_model


async def create_profiles(profile: profile_model.Profiles):
    con = await create_connection()
    statement = await con.fetch(
          "INSERT INTO profile (user_id,first_name,last_name,avatar_icon,avatar_color,image_url,created_at,updated_at,deleted_at) VALUES ($1,$2,$3,$4,$5,$6,$7,$8,$9) RETURNING id",
            profile.user_id,
            profile.first_name,
            profile.last_name,
            profile.avatar_icon,
            profile.avatar_color,
            profile.image_url,
            datetime.now(),
            datetime.now(),
            None
        )
    if statement:
        await con.close()
        return ({
            "message" : {
                "id" : ((statement[0].get("id")))
            }
        })

async def get_one_profile(profile_id):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM profile WHERE id = $1 AND deleted_at IS NULL",
        profile_id
    )
    await con.close()
    return statement

# async def get_profile_by_user_id(user_id):
#     con = await create_connection()
#     statement = await con.fetch(
#         "SELECT * FROM profile WHERE user_id = $1 AND deleted_at IS NULL",
#         user_id
#     )
#     await con.close()
#     return statement

async def get_all_profiles_paginated(page_number, page_size):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM profile WHERE deleted_at IS NULL ORDER BY id DESC LIMIT $1 OFFSET $2",
        page_size,
        (page_number - 1) * page_size
    )
    await con.close()
    return statement

async def update_profiles(profile_id, profile: profile_model.Profiles) :
    con = await create_connection()
    statement = await con.fetch(
        "UPDATE profile SET user_id = $1,first_name = $2,last_name = $3,avatar_icon = $4,avatar_color = $5,image_url = $6,updated_at = $7 WHERE id = $8 RETURNING id",
        profile.user_id,
        profile.first_name,
        profile.last_name,
        profile.avatar_icon,
        profile.avatar_color,
        profile.image_url,
        datetime.now(),
        profile_id
    )
    if statement:
        await con.close()
        return ({
            "message" : {
                "id" : ((statement[0].get("id")))
            }
        })

async def delete_profiles(profile_id):
    con = await create_connection()
    statement = await con.fetch(
        "UPDATE profile SET deleted_at = $1 WHERE id = $2",
        datetime.now(),
        profile_id
    )
    await con.close()
    return statement
