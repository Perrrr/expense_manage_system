from cgi import print_form
from enum import unique
import json
import re
from sre_parse import State
from venv import create
from app.config.database import create_connection
from datetime import date, datetime
import uuid
import asyncpg.exceptions as pg_exceptions
from app.errs.err import err_response
from app.models import department_category_budget as department_category_budget_model

async def create_department_category_budget(department_category_budget: department_category_budget_model.DepartmentCategoryBudget):
    con = await create_connection()
    statement = await con.fetch(
        "INSERT INTO department_category_budget (department_id,category_budget_id,status,created_at,updated_at,deleted_at) VALUES ($1,$2,$3,$4,$5,$6) RETURNING id",
        department_category_budget.department_id,
        department_category_budget.category_budget_id,
        department_category_budget.status,
        datetime.now(),
        datetime.now(),
        None
        )
    await con.close()
    return ({
            "message" : {
                "id" : ((statement[0].get("id"))),
            }
        })
        
async def get_one_department_category_budget(department_category_budget_id):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM department_category_budget WHERE id = $1 AND deleted_at IS NULL",
        department_category_budget_id
    )
    await con.close()
    return statement

async def get_all_department_category_budget_paginated(page_number, page_size):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM department_category_budget WHERE deleted_at IS NULL ORDER BY id DESC LIMIT $1 OFFSET $2",
        page_size,
        (page_number - 1) * page_size
    )
    await con.close()
    return statement

async def update_department_category_budget(department_category_budget_id, department_category_budget: department_category_budget_model.DepartmentCategoryBudget):
    con = await create_connection()
    statement = await con.fetch(
            "UPDATE department_category_budget SET department_id = $1, category_budget_id = $2, status = $3, updated_at = $4 WHERE id = $5 RETURNING id",
            department_category_budget.department_id,
            department_category_budget.category_budget_id,
            department_category_budget.status,
            datetime.now(),
            department_category_budget_id
        )
    await con.close()
    return ({
            "message":{
                "id":((statement[0].get("id")))
            }
        })
    
async def delete_department_category_budget(department_category_budget_id):
    con = await create_connection()
    statement = await con.fetch(
        "UPDATE department_category_budget SET deleted_at = $1 WHERE id = $2",
        datetime.now(),
        department_category_budget_id
    )
    await con.close()
    return statement

