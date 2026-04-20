from fastapi import FastAPI
import pandas as pd
import joblib

app = FastAPI()

# Load pipeline
pipeline = joblib.load("diabetes_pipeline.pkl")


@app.get("/")
def home():
    return {"message": "API is running"}


@app.post("/predict")
def predict(data: dict):
    try:
        df = pd.DataFrame([data])

        print("INPUT DF:", df)

        prediction = pipeline.predict(df)

        print("RAW PRED:", prediction)

        return {
            "prediction": str(prediction[0])
        }

    except Exception as e:
        return {
            "error": str(e),
            "type": str(type(e))
        }

