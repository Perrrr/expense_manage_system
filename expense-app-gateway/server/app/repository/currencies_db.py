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
from app.models import currencies as currencie_model

async def create_currencies(currencie: currencie_model.Currencies):
    con = await create_connection()
    statement = await con.fetch(
        "INSERT INTO currencies (public_id,organization_id,name,code,symbol,created_at,updated_at,deleted_at) VALUES ($1,$2,$3,$4,$5,$6,$7,$8) RETURNING id",
        str(uuid.uuid4()),
        currencie.organization_id,
        currencie.name,
        currencie.code,
        currencie.symbol,
        datetime.now(),
        datetime.now(),
        None
        )
    if statement :
        await con.close()
        return ({
            "message" : {
                "id" : ((statement[0].get("id"))),
            }
        })
        
async def get_one_currencie(currencie_id):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM currencies WHERE id = $1 AND deleted_at IS NULL",
        currencie_id
    )
    await con.close()
    return statement

async def get_all_currencies_paginated(page_number, page_size):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM currencies WHERE deleted_at IS NULL ORDER BY id DESC LIMIT $1 OFFSET $2",
        page_size,
        (page_number - 1) * page_size
    )
    await con.close()
    return statement

async def update_currencies(currencie_id, currencie: currencie_model.Currencies):
    con = await create_connection()
    statement = await con.fetch(
            "UPDATE currencies SET organization_id = $1,name = $2,code = $3,symbol = $4,updated_at = $5 WHERE id = $6 RETURNING id",
            currencie.organization_id,
            currencie.name,
            currencie.code,
            currencie.symbol,
            datetime.now(),
            currencie_id
        )
    if statement:
        await con.close()
        return ({
            "message":{
                "id":((statement[0].get("id")))
            }
        })
    
async def delete_currencies(currencie_id):
    con = await create_connection()
    statement = await con.fetch(
        "UPDATE currencies SET deleted_at = $1 WHERE id = $2",
        datetime.now(),
        currencie_id
    )
    await con.close()
    return statement