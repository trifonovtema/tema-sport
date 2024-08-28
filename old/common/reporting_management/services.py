from .database import SessionLocal, Result
from .pdf_generator import PDFGenerator
from ...base.services import BaseService


class ReportingService(BaseService):
    async def get_results(self, race_id: int):
        async with SessionLocal() as db:
            results = await db.query(Result).filter(Result.race_id == race_id).all()
            return results

    async def generate_pdf(
        self, race_id: int, competition_name: str, competition_date: str
    ):
        results = await self.get_results(race_id)
        pdf_path = PDFGenerator().generate_pdf(results)
        message = {
            "pdf_path": pdf_path,
            "competition_name": competition_name,
            "competition_date": competition_date,
        }
        await self.producer_service.produce_message("pdf_generation", message)
