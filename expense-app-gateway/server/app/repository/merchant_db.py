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
from app.models import merchant as merchant_model


async def create_merchant(merchant: merchant_model.Merchant):
    con = await create_connection()
    statement = await con.fetch(
          "INSERT INTO merchant (name,description,created_at,updated_at,deleted_at) VALUES ($1,$2,$3,$4,$5) RETURNING id",
            merchant.name,
            merchant.description,
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

async def get_one_merchant(merchant_id):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM merchant WHERE id = $1 AND deleted_at IS NULL",
        merchant_id
    )
    await con.close()
    return statement

async def get_all_merchant_paginated(page_number, page_size):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM merchant WHERE deleted_at IS NULL ORDER BY id DESC LIMIT $1 OFFSET $2",
        page_size,
        (page_number - 1) * page_size
    )
    await con.close()
    return statement

async def update_merchant(merchant_id, merchant: merchant_model.Merchant) :
    con = await create_connection()
    statement = await con.fetch(
        "UPDATE merchant SET name = $1,description = $2,updated_at = $3 WHERE id = $4 RETURNING id",
        merchant.name,
        merchant.description,
        datetime.now(),
        merchant_id
    )
    if statement:
        await con.close()
        return ({
            "message" : {
                "id" : ((statement[0].get("id")))
            }
        })

async def delete_merchant(merchant_id):
    con = await create_connection()
    statement = await con.fetch(
        "UPDATE merchant SET deleted_at = $1 WHERE id = $2",
        datetime.now(),
        merchant_id
    )
    await con.close()
    return statement
