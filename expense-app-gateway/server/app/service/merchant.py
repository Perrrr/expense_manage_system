from datetime import datetime
import uuid

from pydantic import BaseModel
from typing import Optional
import uuid
import datetime
from app.service import merchant_service
from app.models import merchant as merchant_model

class MerchantService():
    def __init__(self):
        pass
    def CreateMerchant(self, merchant: merchant_model.CreateMerchantForm):
        return merchant_service.CreateMerhant(merchant)
    def GetOneMerchant(self, merchant_id):
        return merchant_service.GetOneMerchant(merchant_id)
    def GetAllMerchantPaginated(self, page_number, page_size):
        return merchant_service.GetAllMerchantPaginated(page_number,page_size)
    def UpdateMerchant(self, merchant_id, merchant: merchant_model.CreateMerchantForm):
        return merchant_service.UpdateMerchant(merchant_id, merchant)
    def DeleteMerchant(self, merchant_id):
        return merchant_service.DeleteMerchant(merchant_id)