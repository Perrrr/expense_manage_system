from pydantic import BaseModel
from typing import Literal, Optional
from datetime import datetime

class ProjectsLog(BaseModel):
    project_log_id : Optional[int] = None
    project_id : int
    user_id : int
    action : str
    subject : str
    avatar_icon : str
    avatar_color : str
    created_at : datetime
    updated_at : datetime
    deleted_at : datetime
    
class CreateProjectLogForm(BaseModel):
    project_id : int
    user_id : int
    action : str
    subject : str
    avatar_icon : str
    avatar_color : str
    class Config :
        schema_extra = {
            "example":
                {
                    "project_id" : 1,
                    "user_id" : 1,
                    "action" : 1,
                    "subject" : "test",
                    "avatar_icon" : "test",
                    "avatar_color" : "test"
                    
                }
        }