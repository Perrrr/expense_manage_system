from datetime import datetime
import uuid

from pydantic import BaseModel
from typing import Optional
import uuid
import datetime
from app.service import currencies_service
from app.models import currencies as cureencie_model



class CurrenciesService():
    def __init__(self):
        pass
    def CreateCurrencie(self, currencie: cureencie_model.CreateCurrencieForm):
        return currencies_service.CreateCurrencie(currencie)
    def GetOneCurrencie(self, currencie_id):
        return currencies_service.GetOneCurrencie(currencie_id)
    def GetAllCurrenciesPaginated(self, page_number, page_size):
        return currencies_service.GetAllCurrenciesPaginated(page_number, page_size)
    def UpdateCurrencie(self, currencie_id, currencie: cureencie_model.CreateCurrencieForm):
        return currencies_service.UpdateCurrencie(currencie_id, currencie)
    def DeleteCurrencie(self, currencie_id):
        return currencies_service.DeleteCurrencie(currencie_id)
        
