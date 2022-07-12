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
from app.models import projects as project_model


async def create_projects(project: project_model.Projects):
    con = await create_connection()
    tr = con.transaction()
    try:
        await tr.start()
        statement = await con.fetch(
          "INSERT INTO projects (code,public_id,organization_id,avatar_color,avatar_icon,name,description,status,created_at,updated_at,deleted_at) VALUES ($1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11) RETURNING id",
            project.code,
            str(uuid.uuid4()),
            project.organization_id,
            project.avatar_color,
            project.avatar_icon,
            project.name,
            project.description,
            project.status,
            datetime.now(),
            datetime.now(),
            None
        )
    except pg_exceptions.UniqueViolationError as e:
        await tr.rollback()
        await  err_response(
            status_code=409,
            message="code already exists"
        )
    if statement:
        await tr.commit()
        await con.close()
        return ({
            "message" : {
                "id" : ((statement[0].get("id")))
            }
        })

async def get_one_project(project_id):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM projects WHERE id = $1 AND deleted_at IS NULL",
        project_id
    )
    await con.close()
    return statement

async def get_all_projects_paginated(page_number, page_size):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM projects WHERE deleted_at IS NULL ORDER BY id DESC LIMIT $1 OFFSET $2",
        page_size,
        (page_number - 1) * page_size
    )
    await con.close()
    return statement

async def update_projects(project_id, project: project_model.Projects) :
    con = await create_connection()
    statement = await con.fetch(
        "UPDATE projects SET code = $1,organization_id = $2,avatar_color = $3,avatar_icon = $4,name = $5,description = $6,status = $7,updated_at = $8 WHERE id = $9 RETURNING id",
        project.code,
        project.organization_id,
        project.avatar_color,
        project.avatar_icon,
        project.name,
        project.description,
        project.status,
        datetime.now(),
        project_id
    )
    if statement:
        await con.close()
        return ({
            "message" : {
                "id" : ((statement[0].get("id")))
            }
        })

async def delete_projects(project_id):
    con = await create_connection()
    statement = await con.fetch(
        "UPDATE projects SET deleted_at = $1 WHERE id = $2",
        datetime.now(),
        project_id
    )
    await con.close()
    return statement
