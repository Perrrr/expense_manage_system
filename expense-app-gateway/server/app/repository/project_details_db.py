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
from app.models import project_details as project_detail_model


async def create_project_details(project_detail: project_detail_model.ProjectDetails):
    con = await create_connection()
    statement = await con.fetch(
          "INSERT INTO project_details (project_id,bussiness_purpose,duration_start,duration_end,created_at,updated_at,deleted_at) VALUES ($1,$2,$3,$4,$5,$6,$7) RETURNING id",
            project_detail.project_id,
            project_detail.bussiness_purpose,
            project_detail.duration_start,
            project_detail.duration_end,
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

async def get_one_project_detail(project_detail_id):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM project_details WHERE id = $1 AND deleted_at IS NULL",
        project_detail_id
    )
    await con.close()
    return statement

async def get_all_project_detail_paginated(page_number, page_size):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM project_details WHERE deleted_at IS NULL ORDER BY id DESC LIMIT $1 OFFSET $2",
        page_size,
        (page_number - 1) * page_size
    )
    await con.close()
    return statement

async def update_project_detail(project_detail_id, project_detail: project_detail_model.ProjectDetails) :
    con = await create_connection()
    statement = await con.fetch(
        "UPDATE project_details SET project_id = $1,bussiness_purpose = $2,duration_start = $3,duration_end = $4,updated_at = $5 WHERE id = $6 RETURNING id",
        project_detail.project_id,
        project_detail.bussiness_purpose,
        project_detail.duration_start,
        project_detail.duration_end,
        datetime.now(),
        project_detail_id
    )
    if statement:
        await con.close()
        return ({
            "message" : {
                "id" : ((statement[0].get("id")))
            }
        })

async def delete_project_detail(project_detail_id):
    con = await create_connection()
    statement = await con.fetch(
        "UPDATE project_details SET deleted_at = $1 WHERE id = $2",
        datetime.now(),
        project_detail_id
    )
    await con.close()
    return statement
