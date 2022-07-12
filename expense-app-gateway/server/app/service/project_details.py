from app.service import project_details_service
from app.models import project_details as project_detail_model

class ProjectDetailsService():
    def __init__(self):
        pass
    def CreateProjectDetail(self, project_detail:project_detail_model.CreateProjectDetailForm):
        return project_details_service.CreateProjectDetail(project_detail)
    def GetOneProjectDetail(self, project_detail_id):
        return project_details_service.GetOneProjectDetail(project_detail_id)
    def GetAllProjectDetailsPaginated(self, page_number, page_size):
        return project_details_service.GetAllProjectDetailsPaginated(page_number, page_size)
    def UpdateProjectDetail(self, project_detail_id, project_detail: project_detail_model.CreateProjectDetailForm):
        return project_details_service.UpdateProjectDetail(project_detail_id, project_detail)
    def DeleteProjectDetail(self, project_detail_id):
        return project_details_service.DeleteProjectDetail(project_detail_id)