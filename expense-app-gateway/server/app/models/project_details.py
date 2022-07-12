from turtle import update
from pydantic import BaseModel
from typing import Literal, Optional
from datetime import date, datetime

class ProjectDetails(BaseModel):
    project_detail_id : Optional[int] = None
    project_id : int
    bussiness_purpose : str
    duration_start : date
    duration_end : date
    created_at : datetime
    updated_at : datetime
    deleted_at : datetime
    
class CreateProjectDetailForm(BaseModel):
    project_id : int
    bussiness_purpose : str
    duration_start : date
    duration_end : date
    class Config : 
        schema_extra = {
            "example":
                {
                    "project_id" : 1,
                    "bussiness_purpose" : "test",
                    "duration_start" : '2022-12-04',
                    "duration_end" : '2023-12-04'
                }
        }