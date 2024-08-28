from fastapi import FastAPI, Depends
from .routes import router as competition_router
from contextlib import asynccontextmanager
from .services import competition_service, get_competition_service

from .services import CompetitionService


@asynccontextmanager
async def lifespan(app: FastAPI):
    await competition_service.start()
    yield
    await competition_service.stop()


app = FastAPI(lifespan=lifespan)


app.include_router(competition_router, dependencies=[Depends(get_competition_service)])
