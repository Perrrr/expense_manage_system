from sys import prefix
from fastapi import APIRouter 
from app.handler.users import router as user_router 
from app.handler.profiles import router as profile_router
from app.handler.applications import router as application_router
from app.handler.currencies import router as currencie_router
from app.handler.departments_users import router as department_user_router
from app.handler.departments import router as department_router
from app.handler.expense_catagories import router as expense_catagorie_router
from app.handler.expense import router as expense_router
from app.handler.merchant import router as merchant_router
from app.handler.organizations_users_roles import router as organization_user_role_router
from app.handler.organizations_users import router as organization_user_router
from app.handler.organizations import router as organization_router
from app.handler.permissions import router as permission_router
from app.handler.project_details import router as project_detail_router
from app.handler.project_expense import router as project_expense_router
from app.handler.projects_log import router as project_log_router
from app.handler.projects import router as project_router
from app.handler.roles_permissions import router as role_permission_router
from app.handler.roles import router as role_router



router = APIRouter()



router.include_router(user_router, tags= ["users"], prefix= "/user")
router.include_router(profile_router , tags= ["profiles"], prefix= "/profile")
router.include_router(application_router , tags= ["applications"], prefix= "/application")
router.include_router(currencie_router, tags= ["currencies"], prefix= "/currencie")   
router.include_router(department_user_router, tags= ["departments_users"], prefix= "/departments_user")
router.include_router(department_router, tags= ["departments"], prefix= "/departments")
router.include_router(expense_catagorie_router, tags= ["expenses_catagories"], prefix= "/expense_catagorie")
router.include_router(expense_router, tags= ["expenses"],prefix= "/expense")
router.include_router(merchant_router, tags= ["merchants"],prefix= "/merchant")
router.include_router(organization_user_role_router, tags= ["organizations_users_roles"], prefix= "/organization_user_role")
router.include_router(organization_user_router, tags= ["organizations_users"], prefix= "/organization_user")
router.include_router(organization_router, tags= ["organizations"], prefix= "/organization")
router.include_router(permission_router, tags= ["permissions"], prefix= "/permission")
router.include_router(project_detail_router, tags= ["project_details"], prefix= "/project_detail")
router.include_router(project_expense_router, tags= ["project_expenses"], prefix= "/project_expense")
router.include_router(project_log_router, tags= ["projects_log"], prefix= "/project_log")
router.include_router(project_router, tags= ["projects"], prefix= "/project")
router.include_router(role_permission_router, tags= ["roles_permissions"], prefix= "/role_permission")
router.include_router(role_router, tags= ["roles"], prefix= "/role")