from app.repository.organizations_users import OrganizationsUserRepository
from app.models import organizations_users as organization_user_model

OrganizationsUserRepository = OrganizationsUserRepository()

async def CreateOrganizationUser(organization_user: organization_user_model.CreateOrganizationUserForm):
    return await OrganizationsUserRepository.create_organizations_users(organization_user)

async def GetOneOrganizationUser(organization_user_id):
    return await OrganizationsUserRepository.get_one_organization_user(organization_user_id)

async def GetAllOrganizationsUsersPaginated(page_number, page_size):
    return await OrganizationsUserRepository.get_all_organizations_users_paginated(page_number, page_size)

async def UpdateOrganizationUser(organization_user_id, organization_user: organization_user_model.CreateOrganizationUserForm):
    return await OrganizationsUserRepository.update_organizations_users(organization_user_id, organization_user)

async def DeleteOrganizationUser(organization_user_id):
    return await OrganizationsUserRepository.delete_organizations_users(organization_user_id)