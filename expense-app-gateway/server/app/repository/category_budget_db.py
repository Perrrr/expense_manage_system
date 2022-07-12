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
from app.models import category_budget as category_budget_model

async def create_category_budget(category_budget: category_budget_model.CategoryBudget):
    con = await create_connection()
    statement = await con.fetch(
        "INSERT INTO category_budget (budget_id,name,status,avatar_icon,avatar_color,image_url,created_at,updated_at,deleted_at) VALUES ($1,$2,$3,$4,$5,$6,$7,$8,$9) RETURNING id",
        category_budget.budget_id,
        category_budget.name,
        category_budget.status,
        category_budget.avatar_icon,
        category_budget.avatar_color,
        category_budget.image_url,
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
        
async def get_one_category_budget(category_budget_id):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM category_budget WHERE id = $1 AND deleted_at IS NULL",
        category_budget_id
    )
    await con.close()
    return statement

async def get_all_category_budget_paginated(page_number, page_size):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM category_budget WHERE deleted_at IS NULL ORDER BY id DESC LIMIT $1 OFFSET $2",
        page_size,
        (page_number - 1) * page_size
    )
    await con.close()
    return statement

async def update_category_budget(category_budget_id, category_budget: category_budget_model.CategoryBudget):
    con = await create_connection()
    statement = await con.fetch(
            "UPDATE category_budget SET budget_id = $1, name = $2, status = $3, avatar_icon = $4, avatar_color = $5, image_url = $6, updated_at = $7 WHERE id = $8 RETURNING id",
            category_budget.budget_id,
            category_budget.name,
            category_budget.status,
            category_budget.avatar_icon,
            category_budget.avatar_color,
            category_budget.image_url,
            datetime.now(),
            category_budget_id
        )
    await con.close()
    return ({
            "message":{
                "id":((statement[0].get("id")))
            }
        })
    
async def delete_category_budget(category_budget_id):
    con = await create_connection()
    statement = await con.fetch(
        "UPDATE category_budget SET deleted_at = $1 WHERE id = $2",
        datetime.now(),
        category_budget_id
    )
    await con.close()
    return statement

