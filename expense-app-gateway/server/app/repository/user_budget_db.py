from app.config.database import create_connection
from datetime import date, datetime
import uuid
import asyncpg.exceptions as pg_exceptions
from app.errs.err import err_response
from app.models import user_budget as user_budget_model

async def create_user_budget(user_budget: user_budget_model.UserBudget):
    con = await create_connection()
    statement = await con.fetch(
        "INSERT INTO user_budget (budget_id, user_id, status, created_at, updated_at, deleted_at) VALUES ($1,$2,$3,$4,$5,$6) RETURNING id",
        user_budget.budget_id,
        user_budget.user_id,
        user_budget.status,
        datetime.now(),
        datetime.now(),
        None
    )
    await con.close()
    return ({
        "message": {
            "id": ((statement[0].get("id"))),
        }
    })

async def get_one_user_budget(user_budget_id):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM user_budget WHERE id = $1 AND deleted_at IS NULL",
        user_budget_id
    )
    await con.close()
    return statement

async def get_all_user_budget_paginated(page_number, page_size):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM user_budget WHERE deleted_at IS NULL ORDER BY id DESC LIMIT $1 OFFSET $2",
        page_size,
        (page_number - 1) * page_size 
    )
    await con.close()
    return statement

async def update_user_budget(user_budget_id, user_budget: user_budget_model.UserBudget):
    con = await create_connection()
    statement = await con.fetch(
        "UPDATE user_budget SET budget_id = $1, user_id = $2, status = $3, updated_at = $4, WHERE id = $5 RETURNING id",
        user_budget.budget_id,
        user_budget.user_id,
        user_budget.status,
        datetime.now(),
        user_budget_id
    )
    await con.close()
    return ({
        "message": {
            "id": ((statement[0].get("id")))
        }
    })

async def delete_user_budget(user_budget_id):
    con = await create_connection()
    statement = await con.fetch(
        "UPDATE user_budget SET deleted_at = $1 WHERE id = $2",
        datetime.now(),
        user_budget_id 
    )
    await con.close()
    return statement