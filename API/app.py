from fastapi import FastAPI

from pydantic import BaseModel

import pandas as pd

import joblib

app = FastAPI()

model = joblib.load("../Models/rf_ltv_model.pkl")

class CustomerData(BaseModel):

    tenure: int

    MonthlyCharges: float

@app.get("/")
def home():

    return {

        "message": "LTV Prediction API Running"
    }

@app.post("/predict")
def predict(data: CustomerData):

    input_data = pd.DataFrame([{

        'tenure': data.tenure,

        'MonthlyCharges': data.MonthlyCharges
    }])

    prediction = model.predict(input_data)

    return {

        "PredictedLTV": float(prediction[0])
    }