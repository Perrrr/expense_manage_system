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
from app.models import departments as department_model

async def create_departments(department: department_model.Departments):
    con = await create_connection()
    statement = await con.fetch(
            "INSERT INTO departments (public_id,organization_id,name,description,created_at,updated_at,deleted_at) VALUES ($1,$2,$3,$4,$5,$6,$7) RETURNING id",
            str(uuid.uuid4()),
            department.organization_id,
            department.name,
            department.description,
            datetime.now(),
            datetime.now(),
            None
        )
    if statement:
        await con.close()
        return({
            "message" : {
                "id" : ((statement[0].get("id"))),
            }
        })
    
async def get_one_department(department_id):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM departments WHERE id = $1 AND deleted_at IS NULL",
        department_id
    )
    await con.close()
    return statement

async def get_all_departments_paginated(page_number, page_size):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM departments WHERE deleted_at IS NULL ORDER BY id DESC LIMIT $1 OFFSET $2",
        page_size,
        (page_number - 1) * page_size
    )
    await con.close()
    return statement

async def update_departments(department_id, department: department_model.Departments):
    con = await create_connection()
    tr = con.transaction()
    try:
        await tr.start()
        statement = await con.fetch(
            "UPDATE departments SET organization_id = $1,name = $2,description = $3,updated_at = $4 WHERE id = $5 RETURNING id",
            department.organization_id,
            department.name,
            department.description,
            datetime.now(),
            department_id
        )
    except pg_exceptions.UniqueViolationError as e:
        await tr.rollback()
        await  err_response(
            status_code=409,
            message="email already exists"
        )
    if statement:
        await tr.commit()
        await con.close()
        return ({
            "message": {
                "id": ((statement[0].get("id"))),
            }
        })
        
async def delete_departments(department_id):
    con = await create_connection()
    statement = await con.fetch(
        "UPDATE departments SET deleted_at = $1 WHERE id = $2",
        datetime.now(),
        department_id
    )
    await con.close()
    return statement
    