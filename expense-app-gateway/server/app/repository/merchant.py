from datetime import datetime
import profile
from pyexpat import model
import uuid


from pydantic import BaseModel
from typing import Optional
import uuid
import datetime
from app.repository import merchant_db
from app.models import merchant as merchant_model




class MerchantRepository():
    def __init__(self):
        pass
    def create_merchant(self, merchant: merchant_model.Merchant):
        return merchant_db.create_merchant(merchant)
    def get_one_merchant(self, merchant_id):
        return merchant_db.get_one_merchant(merchant_id)
    def get_all_merchant_paginated(self, page_number, page_size):
        return merchant_db.get_all_merchant_paginated(page_number, page_size)
    def update_merchant(self, merchant_id, merchant: merchant_model.Merchant):
        return merchant_db.update_merchant(merchant_id, merchant)
    def delete_merchant(self, merchant_id):
        return merchant_db.delete_merchant(merchant_id)
    