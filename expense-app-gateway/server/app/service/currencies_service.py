from app.repository.currencies import CurrenciesRepository
from app.models import currencies as currencie_model

CurrenciesRepository = CurrenciesRepository()

async def CreateCurrencie(currencie: currencie_model.CreateCurrencieForm):
    return await CurrenciesRepository.create_currencies(currencie)

async def GetOneCurrencie(currencie_id):
    return await CurrenciesRepository.get_one_currencie(currencie_id)

async def GetAllCurrenciesPaginated(page_number, page_size):
    return await CurrenciesRepository.get_all_currencies_paginated(page_number, page_size)

async def UpdateCurrencie(currencie_id, currencie: currencie_model.CreateCurrencieForm):
    return await CurrenciesRepository.update_currencies(currencie_id, currencie)

async def DeleteCurrencie(currencie_id):
    return await CurrenciesRepository.delete_currencies(currencie_id)