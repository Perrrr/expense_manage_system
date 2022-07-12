from cProfile import Profile
from datetime import datetime
import uuid

from pydantic import BaseModel
from typing import Optional
import uuid
import datetime
from app.service import applications_service
from app.models import applications as application_model


class ApplicationService():
    def __init__(self) :
        pass
    def CreateApplication(self, application: application_model.CreateApplicationForm):
        return applications_service.CreateApplication(application)
    def GetOneApplication(self, application_id):
        return applications_service.GetOneApplication(application_id)
    def GetAllApplicationsPaginated(self, page_number, page_size): 
        return applications_service.GetAllapplicationsPaginated(page_number, page_size)
    def UpdateApplication(self, application_id, application: application_model.CreateApplicationForm):
        return applications_service.UpdateApplication(application_id, application)
    def DeleteApplication(self, application_id):
        return applications_service.DeleteApplication(application_id)