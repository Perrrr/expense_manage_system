from enum import unique
import json
import re
from app.config.database import create_connection
from datetime import date, datetime
import uuid
import asyncpg.exceptions as pg_exceptions
from app.errs.err import err_response
from app.models import applications as application_model

async def create_applications(application: application_model.Applications):
    con = await create_connection()
    tr = con.transaction()
    try:
        await tr.start()
        statement = await con.fetch(
            "INSERT INTO application (public_id,name,description,avatar_color,avatar_icon,created_at,updated_at,deleted_at) VALUES ($1,$2,$3,$4,$5,$6,$7,$8) RETURNING id",
            str(uuid.uuid4()),
            application.name,
            application.description,
            application.avatar_color,
            application.avatar_icon,
            datetime.now(),
            datetime.now(),
            None
        )
    except pg_exceptions.UniqueViolationError as e:
        await tr.rollback()
        await  err_response(
            status_code=409,
            message="name already exists"
        )
    if statement :
        await tr.commit()
        await con.close()
        return ({
            "message" : {
                "id" : ((statement[0].get("id"))),
            }
        })
        
async def get_one_application(application_id):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM application WHERE id = $1 AND deleted_at IS NULL",
        application_id
    )
    await con.close()
    return statement

async def get_all_applications_paginated(page_number, page_size):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM application WHERE deleted_at IS NULL ORDER BY id DESC LIMIT $1 OFFSET $2",
        page_size,
        (page_number - 1) * page_size
    )
    await con.close()
    return statement

async def update_applications(application_id,applicaton: application_model.Applications):
    con = await create_connection()
    tr = con.transaction()
    try: 
        await tr.start()
        statement = await con.fetch(
            "UPDATE application SET name = $1,description = $2,avatar_color = $3,avatar_icon = $4,updated_at = $5 WHERE id = $6 RETURNING id",
            applicaton.name,
            applicaton.description,
            applicaton.avatar_color,
            applicaton.avatar_icon,
            datetime.now(),
            application_id
        )
    except pg_exceptions.UniqueViolationError as e:
        await tr.rollback()
        await err_response(
            status_code=409,
            message="name already exists"
        )
    if statement:
        await tr.commit()
        await con.close()
        return ({
            "message":{
                "id":((statement[0].get("id")))
            }
        })
    
async def delete_applications(application_id):
    con = await create_connection()
    statement = await con.fetch(
        "UPDATE application SET deleted_at = $1 WHERE id = $2",
        datetime.now(),
        application_id
    )
    await con.close()
    return statement