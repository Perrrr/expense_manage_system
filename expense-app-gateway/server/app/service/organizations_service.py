from app.repository.organizations import OrganizationsRepository
from app.models import organizations as organization_model

OrganizationsRepository = OrganizationsRepository()

async def CreateOrganization(organization: organization_model.CreateOrganizationForm):
    return await OrganizationsRepository.create_organizations(organization)

async def GetOneOrganization(organization_id):
    return await OrganizationsRepository.get_one_organization(organization_id)

async def GetAllOrganizationsPaginated(page_number, page_size):
    return await OrganizationsRepository.get_all_organizations_paginated(page_number, page_size)

async def UpdateOrganization(organization_id, organization: organization_model.CreateOrganizationForm):
    return await OrganizationsRepository.update_organizations(organization_id, organization)

async def DeleteOrganization(organization_id):
    return await OrganizationsRepository.delete_organizations(organization_id)