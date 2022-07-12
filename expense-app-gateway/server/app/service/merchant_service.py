from app.repository.merchant import MerchantRepository
from app.models import merchant as merchant_model

MerchantRepository = MerchantRepository()

async def CreateMerhant(merchant: merchant_model.CreateMerchantForm):
    return await MerchantRepository.create_merchant(merchant)

async def GetOneMerchant(merchant_id):
    return await MerchantRepository.get_one_merchant(merchant_id)

async def GetAllMerchantPaginated(page_number, page_size):
    return await MerchantRepository.get_all_merchant_paginated(page_number, page_size)

async def UpdateMerchant(merchant_id, merchant: merchant_model.CreateMerchantForm):
    return await MerchantRepository.update_merchant(merchant_id, merchant)

async def DeleteMerchant(merchant_id):
    return await MerchantRepository.delete_merchant(merchant_id)