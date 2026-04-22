from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Create FastAPI app
app = FastAPI()

# Enable CORS (VERY IMPORTANT for React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all for now
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------
# TEST ROUTE (CHECK IF API RUNS)
# -------------------------------
@app.get("/")
def home():
    return {"message": "API is working perfectly 🚀"}

# -------------------------------
# TEST PREDICT ROUTE
# -------------------------------
@app.post("/predict")
def predict(data: dict):
    return {
        "status": "success",
        "received_data": data
    }