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
from app.models import projects_log as project_log_model


async def create_projects_log(project_log: project_log_model.ProjectsLog):
    con = await create_connection()
    statement = await con.fetch(
          "INSERT INTO projects_log (project_id,user_id,action,subject,avatar_icon,avatar_color,created_at,updated_at,deleted_at) VALUES ($1,$2,$3,$4,$5,$6,$7,$8,$9) RETURNING id",
            project_log.project_id,
            project_log.user_id,
            project_log.action,
            project_log.subject,
            project_log.avatar_icon,
            project_log.avatar_color,
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

async def get_one_project_log(project_log_id):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM projects_log WHERE id = $1 AND deleted_at IS NULL",
        project_log_id
    )
    await con.close()
    return statement

async def get_all_projects_log_paginated(page_number, page_size):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM projects_log WHERE deleted_at IS NULL ORDER BY id DESC LIMIT $1 OFFSET $2",
        page_size,
        (page_number - 1) * page_size
    )
    await con.close()
    return statement

async def update_projects_log(project_log_id, project_log: project_log_model.ProjectsLog) :
    con = await create_connection()
    statement = await con.fetch(
        "UPDATE projects_log SET project_id = $1,user_id = $2,action = $3,subject = $4,avatar_icon = $5,avatar_color = $6,updated_at = $7 WHERE id = $8 RETURNING id",
        project_log.project_id,
        project_log.user_id,
        project_log.action,
        project_log.subject,
        project_log.avatar_icon,
        project_log.avatar_color,
        datetime.now(),
        project_log_id
    )
    if statement:
        await con.close()
        return ({
            "message" : {
                "id" : ((statement[0].get("id")))
            }
        })

async def delete_projects_log(project_log_id):
    con = await create_connection()
    statement = await con.fetch(
        "UPDATE projects_log SET deleted_at = $1 WHERE id = $2",
        datetime.now(),
        project_log_id
    )
    await con.close()
    return statement
