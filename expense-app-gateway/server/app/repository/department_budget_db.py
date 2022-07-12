from app.config.database import create_connection
from datetime import date, datetime
import uuid
import asyncpg.exceptions as pg_exceptions
from app.errs.err import err_response
from app.models import department_budget as department_budget_model

async def create_department_budget(department_budget: department_budget_model.DepartmentBudget):
    con = await create_connection()
    statement = await con.fetch(
        "INSERT INTO department_budget (budget_id, department_id, status, created_at, updated_at, deleted_at) VALUES ($1,$2,$3,$4,$5,$6) RETURNING id",
        department_budget.budget_id,
        department_budget.department_id,
        department_budget.status,
        datetime.now(),
        datetime.now(),
        None
    )
    await con.close()
    return ({
        "message": {
            "id": ((statement[0].get("id")))
        }
    })

async def get_one_department_budget(department_budget_id):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM department_budget WHERE id = $1 AND deleted_at IS NULL",
        department_budget_id
    )
    await con.close()
    return statement

async def get_all_department_budget_paginated(page_number, page_size):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM department_budget WHERE deleted_at IS NULL ORDER BY id DESC LIMIT $1 OFFSET $2",
        page_size,
        (page_number - 1) * page_size
    )
    await con.close()
    return statement

async def update_department_budget(department_budget_id, department_budget: department_budget_model.DepartmentBudget):
    con = await create_connection()
    statement = await con.fetch(
        "UPDATE department_budget SET budget_id = $1, departmet_id = $2, status = $3, updated_at = $4 WHERE id = $5 RETURNING id",
        department_budget.budget_id,
        department_budget.department_id,
        department_budget.status,
        datetime.now(),
        department_budget_id
    )
    await con.close()
    return ({
        "message": {
            "id": ((statement[0].get("id")))
        }
    })
    
async def delete_department_budget(department_budget_id):
    con = await create_connection()
    statement = await con.fetch(
        "UPDATE department_budget SET deleted_at = $1, WHERE id = $2",
        datetime.now(),
        department_budget_id
        
    )
    await con.close()
    return statement