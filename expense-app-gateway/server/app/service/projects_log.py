from app.service import projects_log_service
from app.models import projects_log as project_log_model

class ProjectsLogService():
    def __init__(self):
        pass
    def CreateProjectLog(self, project_log: project_log_model.CreateProjectLogForm):
        return projects_log_service.CreateProjectLog(project_log)
    def GetOneProjectLog(self, project_log_id):
        return projects_log_service.GetOneProjectLog(project_log_id)
    def GetAllProjectsLogPaginated(self, page_number, page_size):
        return projects_log_service.GetAllProjectsLogPaginated(page_number, page_size)
    def UpdateProjectLog(self, project_log_id, project_log: project_log_model.CreateProjectLogForm):
        return projects_log_service.UpdateProjectLog(project_log_id, project_log)
    def DeleteProjectLog(self, project_log_id):
        return projects_log_service.DeleteProjectLog(project_log_id)