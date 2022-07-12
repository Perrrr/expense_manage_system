from enum import unique
import json
import re
from app.config.database import create_connection
from datetime import date, datetime
import uuid
import asyncpg.exceptions as pg_exceptions
from app.errs.err import err_response
from app.models import expense as expense_model

async def create_expense(expense: expense_model.Expense):
    con = await create_connection()
    statement = await con.fetch(
        "INSERT INTO expense (public_id,expense_category_id,cliam_reimbursement,description,reference_number,currency_id,merchant_id,amount,user_id,created_at,updated_at,deleted_at) VALUES ($1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12) RETURNING id",
        str(uuid.uuid4()),
        expense.expense_category_id,
        expense.cliam_reimbursement,
        expense.description,
        expense.reference_number,
        expense.currency_id,
        expense.merchant_id,
        expense.amount,
        expense.user_id,
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
    

async def get_one_expense(expense_id):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM expense WHERE id = $1 AND deleted_at IS NULL",
        expense_id
    )
    await con.close()
    return statement

async def get_all_expense_paginated(page_number, page_size):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM expense WHERE deleted_at IS NULL ORDER BY id DESC LIMIT $1 OFFSET $2",
        page_size,
        (page_number - 1) * page_size
    )
    await con.close()
    return statement


async def update_expense(expense_id,expense: expense_model.Expense):
    con = await create_connection()
    statement = await con.fetch(
            "UPDATE expense SET expense_category_id = $1,cliam_reimbursement = $2,description = $3,reference_number = $4,currency_id = $5,merchant_id = $6,amount = $7,user_id = $8,updated_at = $9 WHERE id = $10 RETURNING id",
            expense.expense_category_id,
            expense.cliam_reimbursement,
            expense.description,
            expense.reference_number,
            expense.currency_id,
            expense.merchant_id,
            expense.amount,
            expense.user_id,
            datetime.now(),
            expense_id
        )
    if statement:
        await con.close()
        return ({
            "message": {
                "id": ((statement[0].get("id"))),
            }
        })
        
        
async def delete_expense(expense_id):
    con = await create_connection()
    statement = await con.fetch(
        "UPDATE expense SET deleted_at = $1 WHERE id = $2",
        datetime.now(),
        expense_id
    )
    await con.close()
    return statement
    