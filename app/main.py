from fastapi import FastAPI, HTTPException, Request, Depends
from pydantic import BaseModel
from sklearn.ensemble import RandomForestClassifier
import joblib
import numpy as np
import uvicorn
import logging

# Logging config
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define app
app = FastAPI(title="🚀 ML Model API - Scikit-learn + FastAPI")

# Load model
model = joblib.load("model/model.pkl")

# Authentication dependency
def verify_token(request: Request):
    token = request.headers.get("Authorization")
    if token != "Bearer your-secret-token":
        raise HTTPException(status_code=401, detail="Unauthorized")

# Input model
class InputData(BaseModel):
    features: list[float]

@app.post("/predict", dependencies=[Depends(verify_token)])
def predict(data: InputData):
    try:
        X = np.array(data.features).reshape(1, -1)
        prediction = model.predict(X)
        logger.info(f"Prediction request: {data.features} -> {prediction.tolist()}")
        return {"prediction": prediction.tolist()}
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
