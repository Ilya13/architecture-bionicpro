
from fastapi import APIRouter, Depends

from app.api.models.responses import Report
from app.dependencies import RoleChecker


reports = [
    {
        "sensorId": 1,
        "measure": 123
    },
    {
        "sensorId": 2,
        "measure": 444
    },
    {
        "sensorId": 3,
        "measure": 888
    },
    {
        "sensorId": 4,
        "measure": 1024
    }
]


router = APIRouter()


@router.get(
    path='/reports',
    tags=['Reports'],
    description='Получение отчетов',
    dependencies=[Depends(RoleChecker(allowed_roles=["prothetic_user"]))]
)
async def get_reports() -> dict:
    return { "data": reports }

