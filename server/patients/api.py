from fastapi import APIRouter, HTTPException
from patients.models import Patient
from db import patients_collection
from typing import List

router = APIRouter()

@router.post("/", response_model=Patient)
def create_patient(patient: Patient):
    patients_collection.insert_one(patient.dict())
    return patient

@router.get("/", response_model=List[Patient])
def list_patients():
    patients = list(patients_collection.find())
    return patients

@router.get("/{patient_id}", response_model=Patient)
def get_patient(patient_id: str):
    patient = patients_collection.find_one({"_id": patient_id})
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

@router.put("/{patient_id}", response_model=Patient)
def update_patient(patient_id: str, updated_patient: Patient):
    result = patients_collection.update_one({"_id": patient_id}, {"$set": updated_patient.dict()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Patient not found")
    return updated_patient

@router.delete("/{patient_id}")
def delete_patient(patient_id: str):
    result = patients_collection.delete_one({"_id": patient_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Patient not found")
    return {"message": "Patient deleted successfully"}
