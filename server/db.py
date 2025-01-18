# server/db.py
from pymongo import MongoClient

client = MongoClient("mongodb://mongodb:27017/")
db = client.medical_db

# Collections for convenience
patients_collection = db.patients
