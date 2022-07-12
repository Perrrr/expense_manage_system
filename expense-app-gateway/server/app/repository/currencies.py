from datetime import datetime
import profile
from pyexpat import model
import uuid


from pydantic import BaseModel
from typing import Optional
import uuid
import datetime
from app.repository import currencies_db
from app.models import currencies as currencie_model




class CurrenciesRepository():
    def __init__(self):
        pass
    def create_currencies(self, currencie: currencie_model.Currencies):
        return currencies_db.create_currencies(currencie)
    def get_one_currencie(self, currencie_id):
        return currencies_db.get_one_currencie(currencie_id)
    def get_all_currencies_paginated(self, page_number, page_size):
        return currencies_db.get_all_currencies_paginated(page_number, page_size)
    def update_currencies(self, currencie_id, currencie: currencie_model.Currencies):
        return currencies_db.update_currencies(currencie_id, currencie)
    def delete_currencies(self, currencie_id):
        return currencies_db.delete_currencies(currencie_id)
    