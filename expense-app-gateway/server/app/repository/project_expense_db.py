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
from app.models import project_expense as project_expense_model


async def create_project_expense(project_expense: project_expense_model.ProjectExpense):
    con = await create_connection()
    statement = await con.fetch(
          "INSERT INTO project_expense (project_id,expense_id,created_at,updated_at,deleted_at) VALUES ($1,$2,$3,$4,$5) RETURNING id",
            project_expense.project_id,
            project_expense.expense_id,
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

async def get_one_project_expense(project_expense_id):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM project_expense WHERE id = $1 AND deleted_at IS NULL",
        project_expense_id
    )
    await con.close()
    return statement

async def get_all_project_expense_paginated(page_number, page_size):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM project_expense WHERE deleted_at IS NULL ORDER BY id DESC LIMIT $1 OFFSET $2",
        page_size,
        (page_number - 1) * page_size
    )
    await con.close()
    return statement

async def update_project_expense(project_expense_id, project_expense: project_expense_model.ProjectExpense) :
    con = await create_connection()
    statement = await con.fetch(
        "UPDATE project_expense SET project_id = $1,expense_id = $2,updated_at = $3 WHERE id = $4 RETURNING id",
        project_expense.project_id,
        project_expense.expense_id,
        datetime.now(),
        project_expense_id
    )
    if statement:
        await con.close()
        return ({
            "message" : {
                "id" : ((statement[0].get("id")))
            }
        })

async def delete_project_expense(project_expense_id):
    con = await create_connection()
    statement = await con.fetch(
        "UPDATE project_expense SET deleted_at = $1 WHERE id = $2",
        datetime.now(),
        project_expense_id
    )
    await con.close()
    return statement
