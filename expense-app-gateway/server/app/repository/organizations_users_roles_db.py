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
from app.models import organizations_users_roles as organization_user_role_model

async def create_organizations_users_roles(organization_user_role: organization_user_role_model.OrganizationsUsersRoles):
    con = await create_connection()
    statement = await con.fetch(
            "INSERT INTO organizations_users_roles (organization_id,application_id,user_id,role_id,created_at,updated_at,deleted_at) VALUES ($1,$2,$3,$4,$5,$6,$7) RETURNING id",
            organization_user_role.organization_id,
            organization_user_role.application_id,
            organization_user_role.user_id,
            organization_user_role.role_id,
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
    
async def get_one_organization_user_role(organization_user_role_id):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM organizations_users_roles WHERE id = $1 AND deleted_at IS NULL",
        organization_user_role_id
    )
    await con.close()
    return statement

async def get_all_organizations_users_roles_paginated(page_number, page_size):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM organizations_users_roles WHERE deleted_at IS NULL ORDER BY id DESC LIMIT $1 OFFSET $2",
        page_size,
        (page_number - 1) * page_size
    )
    await con.close()
    return statement

async def update_organization_user_role(organization_user_role_id,organization_user_role: organization_user_role_model.OrganizationsUsersRoles):
    con = await create_connection()
    statement = await con.fetch(
            "UPDATE organizations_users_roles SET organization_id = $1,application_id = $2,user_id = $3,role_id = $4,updated_at = $5 WHERE id = $6 RETURNING id",
            organization_user_role.organization_id,
            organization_user_role.application_id,
            organization_user_role.user_id,
            organization_user_role.role_id,
            datetime.now(),
            organization_user_role_id
        )
    await con.close()
    return ({
            "message": {
                "id": ((statement[0].get("id"))),
            }
        })
        
async def delete_organizations_users_roles(organization_user_role_id):
    con = await create_connection()
    statement = await con.fetch(
        "UPDATE organizations_users_roles SET deleted_at = $1 WHERE id = $2",
        datetime.now(),
        organization_user_role_id
    )
    await con.close()
    return statement
    