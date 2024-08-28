from fastapi import APIRouter
from .services import ReportingService

router = APIRouter()
reporting_service = ReportingService()


@router.get("/results")
async def get_results_endpoint(race_id: int):
    return await reporting_service.get_results(race_id)


@router.get("/results/pdf")
async def generate_pdf_results(
    race_id: int, competition_name: str, competition_date: str
):
    await reporting_service.generate_pdf(race_id, competition_name, competition_date)
    return {"message": "PDF generation request sent"}
