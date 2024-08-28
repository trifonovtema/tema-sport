from fastapi import FastAPI
from .routes import router as reporting_router

app = FastAPI()
app.include_router(reporting_router)
