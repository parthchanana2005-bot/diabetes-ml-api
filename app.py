from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import joblib
import os
import numpy as np

# Initialize FastAPI app
app = FastAPI()

# 🔥 CORS FIX (VERY IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all origins (React localhost + deployed frontend)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model files safely
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, "classification_model.pkl"))
pipeline = joblib.load(os.path.join(BASE_DIR, "diabetes_pipeline.pkl"))

# Input schema (ALL FEATURES)
class InputData(BaseModel):
    pregnancies: float
    glucose: float
    blood_pressure: float
    skin_thickness: float
    insulin: float
    bmi: float
    diabetes_pedigree_function: float
    age: float
    glucose_postprandial: float
    hba1c: float
    insulin_level: float
    diabetes_risk_score: float
    waist_to_hip_ratio: float
    heart_rate: float
    triglycerides: float
    diet_score: float
    cardiovascular_history: float
    alcohol_consumption_per_week: float
    physical_activity_minutes_per_week: float
    screen_time: float

# Test route
@app.get("/")
def home():
    return {"message": "API is running successfully 🚀"}

# Prediction route
@app.post("/predict")
def predict(data: InputData):
    try:
        input_dict = data.dict()

        # Convert input to array
        input_values = np.array([list(input_dict.values())])

        # Apply pipeline
        transformed = pipeline.transform(input_values)

        # Predict
        prediction = model.predict(transformed)

        return {
            "prediction": int(prediction[0]),
            "status": "success"
        }

    except Exception as e:
        return {
            "error": str(e),
            "status": "failed"
        }