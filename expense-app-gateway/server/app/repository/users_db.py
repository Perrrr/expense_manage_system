from enum import unique
import json
import re
from app.config.database import create_connection
from datetime import date, datetime
import uuid
import asyncpg.exceptions as pg_exceptions
from app.errs.err import err_response
from app.models import users as user_model



async def create_users(user: user_model.Users ):
    con = await create_connection()
    tr = con.transaction()
    try:
        await tr.start()
        statement = await con.fetch(
            "INSERT INTO users  (public_id,email,password,prefix_mobile,mobile_number,activated,note,created_at,updated_at,deleted_at) VALUES ($1,$2,$3,$4,$5,$6,$7,$8,$9,$10) RETURNING id",
            str(uuid.uuid4()),
            user.email,
            user.prefix_mobile,
            user.mobile_number,
            user.activated,
            user.note,
            datetime.now(),
            datetime.now(),
            None
        )
    except pg_exceptions.UniqueViolationError as e:
        await tr.rollback()
        await  err_response(
            status_code=409,
            message="email or mobile number already exists"
        )
    if statement:
        await tr.commit()
        await con.close()
        return ({
            "message": {
                "id": ((statement[0].get("id"))),
            }
        })

async def get_one_user(user_id):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM users WHERE id = $1 AND deleted_at IS NULL",
        user_id
    )
    await con.close()
    return statement

async def get_all_users_paginated(page_number, page_size):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM users WHERE deleted_at IS NULL ORDER BY id DESC LIMIT $1 OFFSET $2",
        page_size,
        (page_number - 1) * page_size
    )
    await con.close()
    return statement

async def update_users(user_id, user: user_model.Users ):
    con = await create_connection()
    tr = con.transaction()
    try:
        await tr.start()
        statement = await con.fetch(
            "UPDATE users SET email = $1, password = $2, prefix_mobile = $3, mobile_number = $4, activated = $5, updated_at = $6 WHERE id = $7 RETURNING id",
            user.email,
            user.password,
            user.prefix_mobile,
            user.mobile_number,
            user.activated,
            datetime.now(),
            user_id
        )
    except pg_exceptions.UniqueViolationError as e:
        await tr.rollback()
        await  err_response(
            status_code=409,
            message="email or mobile number already exists"
        )
    if statement:
        await tr.commit()
        await con.close()
        return ({
            "message": {
                "id": ((statement[0].get("id"))),
            }
        })
    
async def delete_users(user_id):
    con = await create_connection()
    statement = await con.fetch(
        "UPDATE users SET deleted_at = $1 WHERE id = $2",
        datetime.now(),
        user_id
    )
    await con.close()
    return statement
    
