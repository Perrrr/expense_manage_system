from datetime import datetime
import uuid


from pydantic import BaseModel
from typing import Optional
import uuid
import datetime
from app.repository import applications_db
from app.models import applications as application_model




class ApplicationsRepository():
    def __init__(self):
        pass
    def create_applications(self, application: application_model.Applications):
        return applications_db.create_applications(application)
    def get_one_application(self, application_id):
        return applications_db.get_one_application(application_id)
    def get_all_applications_paginated(self, page_number, page_size):
        return applications_db.get_all_applications_paginated(page_number, page_size)
    def update_applications(self, application_id, application: application_model.Applications):
        return applications_db.update_applications(application_id, application)
    def delete_applications(self, application_id):
        return applications_db.delete_applications(application_id)
    