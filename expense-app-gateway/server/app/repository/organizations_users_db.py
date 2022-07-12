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
from app.models import organizations_users as organization_user_model

async def create_organizations_users(organization_user: organization_user_model.OrganizationsUsers):
    con = await create_connection()
    statement = await con.fetch(
            "INSERT INTO organizations_users (organization_id,application_id,user_id,created_at,updated_at,deleted_at) VALUES ($1,$2,$3,$4,$5,$6) RETURNING id",
            organization_user.organization_id,
            organization_user.application_id,
            organization_user.user_id,
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
    
async def get_one_organization_user(organization_user_id):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM organizations_users WHERE id = $1 AND deleted_at IS NULL",
        organization_user_id
    )
    await con.close()
    return statement

async def get_all_organizations_users_paginated(page_number, page_size):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM organizations_users WHERE deleted_at IS NULL ORDER BY id DESC LIMIT $1 OFFSET $2",
        page_size,
        (page_number - 1) * page_size
    )
    await con.close()
    return statement

async def update_organization_user(organization_user_id,organization_user: organization_user_model.OrganizationsUsers):
    con = await create_connection()
    statement = await con.fetch(
            "UPDATE organizations_users SET organization_id = $1,application_id = $2,user_id = $3,updated_at = $4 WHERE id = $5 RETURNING id",
            organization_user.organization_id,
            organization_user.application_id,
            organization_user.user_id,
            datetime.now(),
            organization_user_id
        )
    await con.close()
    return ({
            "message": {
                "id": ((statement[0].get("id"))),
            }
        })
        
async def delete_organizations_users(organization_user_id):
    con = await create_connection()
    statement = await con.fetch(
        "UPDATE organizations_users SET deleted_at = $1 WHERE id = $2",
        datetime.now(),
        organization_user_id
    )
    await con.close()
    return statement
    