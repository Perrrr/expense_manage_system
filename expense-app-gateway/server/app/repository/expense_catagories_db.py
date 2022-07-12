from enum import unique
import json
import re
from app.config.database import create_connection
from datetime import date, datetime
import uuid
import asyncpg.exceptions as pg_exceptions
from app.errs.err import err_response
from app.models import expense_catagories as expense_catagories_model



async def create_expense_categories(expense_catagorie: expense_catagories_model.ExpenseCatagories ):
    con = await create_connection()
    statement = await con.fetch(
            "INSERT INTO expense_categories (public_id,organization_id,avatar_icon,avatar_color,name,description,created_at,updated_at,deleted_at) VALUES ($1,$2,$3,$4,$5,$6,$7,$8,$9) RETURNING id",
            str(uuid.uuid4()),
            expense_catagorie.organization_id,
            expense_catagorie.avatar_icon,
            expense_catagorie.avatar_color,
            expense_catagorie.name,
            expense_catagorie.description,
            datetime.now(),
            datetime.now(),
            None
        )
    if statement:
        await con.close()
        return ({
            "message": {
                "id": ((statement[0].get("id"))),
            }
        })

async def get_one_expense_catagorie(expense_catagorie_id):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM expense_categories WHERE id = $1 AND deleted_at IS NULL",
        expense_catagorie_id
    )
    await con.close()
    return statement

async def get_all_expense_categories_paginated(page_number, page_size):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM expense_categories WHERE deleted_at IS NULL ORDER BY id DESC LIMIT $1 OFFSET $2",
        page_size,
        (page_number - 1) * page_size
    )
    await con.close()
    return statement

async def update_expense_categories(expense_catagorie_id,expense_catagorie: expense_catagories_model.ExpenseCatagories):
    con = await create_connection()
    statement = await con.fetch(
            "UPDATE expense_categories SET organization_id = $1,avatar_icon = $2,avatar_color = $3,name = $4,description = $5,updated_at = $6 WHERE id = $7 RETURNING id",
            expense_catagorie.organization_id,
            expense_catagorie.avatar_icon,
            expense_catagorie.avatar_color,
            expense_catagorie.name,
            expense_catagorie.description,
            datetime.now(),
            expense_catagorie_id
        )
    if statement:
        await con.close()
        return ({
            "message": {
                "id": ((statement[0].get("id"))),
            }
        })
    
async def delete_expense_categories(expense_catagorie_id):
    con = await create_connection()
    statement = await con.fetch(
        "UPDATE expense_categories SET deleted_at = $1 WHERE id = $2",
        datetime.now(),
        expense_catagorie_id
    )
    await con.close()
    return statement
    




