# server/patients/models.py
from pydantic import BaseModel
from typing import List

class Medicine(BaseModel):
    date: str
    type: str
    dose: str
    supplemental_type: str

class Treatment(BaseModel):
    start_date: str
    end_date: str
    treatment_type: str
    medicines: List[Medicine] = []

class Patient(BaseModel):
    name: str
    date_of_birth: str
    sex: str
    contact_info: str
    representative_contact_info: str
    treatments: List[Treatment] = []
