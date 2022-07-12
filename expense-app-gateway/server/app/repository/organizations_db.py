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
from app.models import organizations as organization_model

async def create_organizations(organization: organization_model.Organizations):
    con = await create_connection()
    tr = con.transaction()
    try:
        await tr.start()
        statement = await con.fetch(
            "INSERT INTO organizations (public_id,name,code,avatar_icon,avatar_color,image_url,description,created_at,updated_at,deleted_at) VALUES ($1,$2,$3,$4,$5,$6,$7,$8,$9,$10) RETURNING id",
            str(uuid.uuid4()),
            organization.name,
            organization.code,
            organization.avatar_icon,
            organization.avatar_color,
            organization.image_url,
            organization.description,
            datetime.now(),
            datetime.now(),
            None
        )
    except pg_exceptions.UniqueViolationError as e:
        await tr.rollback()
        await err_response(
            status_code=409,
            message="code already exists"
        )
    if statement:
        await tr.commit()
        await con.close()
        return({
            "message" : {
                "id" : ((statement[0].get("id"))),
            }
        })
    
async def get_one_organization(organization_id):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM organizations WHERE id = $1 AND deleted_at IS NULL",
        organization_id
    )
    await con.close()
    return statement

async def get_all_organizations_paginated(page_number, page_size):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM organizations WHERE deleted_at IS NULL ORDER BY id DESC LIMIT $1 OFFSET $2",
        page_size,
        (page_number - 1) * page_size
    )
    await con.close()
    return statement

async def update_organizations(organization_id,organization: organization_model.Organizations):
    con = await create_connection()
    tr = con.transaction()
    try:
        await tr.start()
        statement = await con.fetch(
            "UPDATE organizations SET name = $1,code = $2,avatar_icon = $3,avatar_color = $4,image_url = $5,description = $6,updated_at = $7 WHERE id = $8 RETURNING id",
            organization.name,
            organization.code,
            organization.avatar_icon,
            organization.avatar_color,
            organization.image_url,
            organization.description,
            datetime.now(),
            organization_id
        )
    except pg_exceptions.UniqueViolationError as e:
        await tr.rollback()
        await  err_response(
            status_code=409,
            message="email already exists"
        )
    if statement:
        await tr.commit()
        await con.close()
        return ({
            "message": {
                "id": ((statement[0].get("id"))),
            }
        })
        
async def delete_organizations(organization_id):
    con = await create_connection()
    statement = await con.fetch(
        "UPDATE organizations SET deleted_at = $1 WHERE id = $2",
        datetime.now(),
        organization_id
    )
    await con.close()
    return statement
    