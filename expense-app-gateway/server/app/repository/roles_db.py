from cgi import print_form
from enum import unique
import json
from venv import create
from app.config.database import create_connection
from datetime import date, datetime
import uuid
import asyncpg.exceptions as pg_exceptions
from app.errs.err import err_response
from app.models import roles as role_model


async def create_roles(role: role_model.Roles):
    con = await create_connection()
    statement = await con.fetch(
          "INSERT INTO roles (public_id,application_id,name,description,created_at,updated_at,deleted_at) VALUES ($1,$2,$3,$4,$5,$6,$7) RETURNING id",
            str(uuid.uuid4()),
            role.application_id,
            role.name,
            role.description,
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

async def get_one_role(role_id):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM roles WHERE id = $1 AND deleted_at IS NULL",
        role_id
    )
    await con.close()
    return statement

async def get_all_roles_paginated(page_number, page_size):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM roles WHERE deleted_at IS NULL ORDER BY id DESC LIMIT $1 OFFSET $2",
        page_size,
        (page_number - 1) * page_size
    )
    await con.close()
    return statement

async def update_roles(role_id, role: role_model.Roles) :
    con = await create_connection()
    statement = await con.fetch(
        "UPDATE roles SET application_id = $1,name = $2,description = $3,updated_at = $4 WHERE id = $5 RETURNING id",
        role.application_id,
        role.name,
        role.description,
        datetime.now(),
        role_id
    )
    if statement:
        await con.close()
        return ({
            "message" : {
                "id" : ((statement[0].get("id")))
            }
        })

async def delete_roles(role_id):
    con = await create_connection()
    statement = await con.fetch(
        "UPDATE roles SET deleted_at = $1 WHERE id = $2",
        datetime.now(),
        role_id
    )
    await con.close()
    return statement
