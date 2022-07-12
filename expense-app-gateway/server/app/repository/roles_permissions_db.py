from cgi import print_form
from enum import unique
import json
from venv import create
from app.config.database import create_connection
from datetime import date, datetime
import uuid
import asyncpg.exceptions as pg_exceptions
from app.errs.err import err_response
from app.models import roles_permissions as role_permission_model


async def create_roles_permissions(role_permission: role_permission_model.RolesPermissions):
    con = await create_connection()
    statement = await con.fetch(
          "INSERT INTO roles_permissions (application_id,role_id,permission_id,created_at,updated_at,deleted_at) VALUES ($1,$2,$3,$4,$5,$6) RETURNING id",
            role_permission.application_id,
            role_permission.role_id,
            role_permission.permission_id,
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

async def get_one_role_permission(role_permission_id):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM roles_permissions WHERE id = $1 AND deleted_at IS NULL",
        role_permission_id
    )
    await con.close()
    return statement

async def get_all_roles_permissions_paginated(page_number, page_size):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM roles_permissions WHERE deleted_at IS NULL ORDER BY id DESC LIMIT $1 OFFSET $2",
        page_size,
        (page_number - 1) * page_size
    )
    await con.close()
    return statement

async def update_roles_permissions(role_permission_id, role_permission: role_permission_model.RolesPermissions) :
    con = await create_connection()
    statement = await con.fetch(
        "UPDATE roles_permissions SET application_id = $1,role_id = $2,permission_id = $3,updated_at = $4 WHERE id = $5 RETURNING id",
        role_permission.application_id,
        role_permission.role_id,
        role_permission.permission_id,
        datetime.now(),
        role_permission_id
    )
    if statement:
        await con.close()
        return ({
            "message" : {
                "id" : ((statement[0].get("id")))
            }
        })

async def delete_roles_permissions(role_permission_id):
    con = await create_connection()
    statement = await con.fetch(
        "UPDATE roles_permissions SET deleted_at = $1 WHERE id = $2",
        datetime.now(),
        role_permission_id
    )
    await con.close()
    return statement
