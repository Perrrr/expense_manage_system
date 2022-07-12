from app.service import projects_service
from app.models import projects as project_model

class ProjectsService():
    def __init__(self):
        pass
    def CreateProject(self, project: project_model.CreateProjectForm):
        return projects_service.CreateProject(project)
    def GetOneProject(self, project_id):
        return projects_service.GetOneProject(project_id)
    def GetAllProjectsPaginated(self, page_number, page_size):
        return projects_service.GetAllProjectsPaginated(page_number, page_size)
    def UpdateProject(self, project_id, project: project_model.CreateProjectForm):
        return projects_service.UpdateProject(project_id, project)
    def DeleteProject(self, project_id):
        return projects_service.DeleteProject(project_id)   