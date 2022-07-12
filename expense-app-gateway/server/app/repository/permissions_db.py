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
from app.models import permissions as permission_model


async def create_permissions(permission: permission_model.Permissions):
    con = await create_connection()
    statement = await con.fetch(
          "INSERT INTO permissions (application_id,public_id,name,method,description,created_at,updated_at,deleted_at) VALUES ($1,$2,$3,$4,$5,$6,$7,$8) RETURNING id",
            permission.application_id,
            str(uuid.uuid4()),
            permission.name,
            permission.method,
            permission.description,
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

async def get_one_permission(permission_id):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM permissions WHERE id = $1 AND deleted_at IS NULL",
        permission_id
    )
    await con.close()
    return statement

async def get_all_permissions_paginated(page_number, page_size):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM permissions WHERE deleted_at IS NULL ORDER BY id DESC LIMIT $1 OFFSET $2",
        page_size,
        (page_number - 1) * page_size
    )
    await con.close()
    return statement

async def update_permissions(permission_id, permission: permission_model.Permissions) :
    con = await create_connection()
    statement = await con.fetch(
        "UPDATE permissions SET application_id = $1,name = $2,method = $3,description =$4,updated_at = $5 WHERE id = $6 RETURNING id",
        permission.application_id,
        permission.name,
        permission.method,
        permission.description,
        datetime.now(),
        permission_id
    )
    if statement:
        await con.close()
        return ({
            "message" : {
                "id" : ((statement[0].get("id")))
            }
        })

async def delete_permissions(permission_id):
    con = await create_connection()
    statement = await con.fetch(
        "UPDATE permissions SET deleted_at = $1 WHERE id = $2",
        datetime.now(),
        permission_id
    )
    await con.close()
    return statement
