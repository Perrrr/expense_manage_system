from fastapi import APIRouter
from app.service import project_expense
from app.models import project_expense as project_expense_model

router = APIRouter()
project_expense_service = project_expense.ProjectExpenseService()

@router.post("/")
async def CreateProjectExpense(project_expense: project_expense_model.CreateProjectExpenseForm):
    return await project_expense_service.CreateProjectExpense(project_expense)

@router.get("/{project_expense_id}")
async def GetOneProjectExpense(project_expense_id: int):
    return await project_expense_service.GetOneProjectExpense(project_expense_id)

@router.get("/")
async def GetAllProjectExpense(page_number: int, page_size: int):
    return await project_expense_service.GetAllProjectExpensePaginated(page_number, page_size)

@router.put("/{project_expense_id}")
async def UpdateProjectExpense(project_expense_id: int, project_expense: project_expense_model.CreateProjectExpenseForm):
    return await project_expense_service.UpdateProjectExpense(project_expense_id, project_expense)

@router.delete("/{project_expense_id}")
async def DeleteProjectExpense(project_expense_id: int):
    return await project_expense_service.DeleteProjectExpense(project_expense_id)