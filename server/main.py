# server/main.py
from fastapi import FastAPI
from patients.api import router as patient_router

app = FastAPI()

app.include_router(patient_router, prefix="/patients", tags=["patients"])