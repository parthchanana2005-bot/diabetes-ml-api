from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import joblib

# Initialize app
app = FastAPI()

# ✅ CORS FIX (VERY IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all (frontend connection fix)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Load model
model = joblib.load("classification_model.pkl")

# ✅ Home route
@app.get("/")
def home():
    return {"message": "Diabetes ML API is running"}

# ✅ Prediction route
@app.post("/predict")
def predict(data: dict):
    try:
        # Convert input to DataFrame
        df = pd.DataFrame([data])

        # Expected columns (VERY IMPORTANT)
        required_columns = [
            "pregnancies",
            "glucose",
            "blood_pressure",
            "skin_thickness",
            "insulin",
            "bmi",
            "diabetes_pedigree_function",
            "age",
            "glucose_postprandial",
            "hba1c",
            "insulin_level",
            "diabetes_risk_score"
        ]

        # Check missing columns
        missing = set(required_columns) - set(df.columns)
        if missing:
            return {
                "error": f"Missing columns: {missing}"
            }

        # Ensure correct column order
        df = df[required_columns]

        # Prediction
        prediction = model.predict(df)

        return {
            "prediction": int(prediction[0])
        }

    except Exception as e:
        return {
            "error": str(e)
        }