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
from app.models import departments_users as department_user_model

async def create_departments_users(department_user: department_user_model.DepartmentsUsers):
    con = await create_connection()
    statement = await con.fetch(
            "INSERT INTO departments_users (department_id,user_id,created_at,updated_at,deleted_at) VALUES ($1,$2,$3,$4,$5) RETURNING id",
            department_user.department_id,
            department_user.user_id,
            datetime.now(),
            datetime.now(),
            None
        )
    if statement:
        await con.close()
        return({
            "message" : {
                "id" : ((statement[0].get("id"))),
            }
        })
    
async def get_one_department_user(department_user_id):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM departments_users WHERE id = $1 AND deleted_at IS NULL",
        department_user_id
    )
    await con.close()
    return statement

async def get_all_departments_users_paginated(page_number, page_size):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM departments_users WHERE deleted_at IS NULL ORDER BY id DESC LIMIT $1 OFFSET $2",
        page_size,
        (page_number - 1) * page_size
    )
    await con.close()
    return statement

async def update_departments_users(department_user_id,department_user: department_user_model.DepartmentsUsers):
    con = await create_connection()
    statement = await con.fetch(
            "UPDATE departments_users SET department_id = $1,user_id = $2,updated_at = $3 WHERE id = $4 RETURNING id",
            department_user.department_id,
            department_user.user_id,
            datetime.now(),
            department_user_id
        )
    if statement:
        await con.close()
        return ({
            "message": {
                "id": ((statement[0].get("id"))),
            }
        })
        
async def delete_departments_users(department_user_id):
    con = await create_connection()
    statement = await con.fetch(
        "UPDATE departments_users SET deleted_at = $1 WHERE id = $2",
        datetime.now(),
        department_user_id
    )
    await con.close()
    return statement
    