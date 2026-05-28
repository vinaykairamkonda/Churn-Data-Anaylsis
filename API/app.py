from fastapi import FastAPI, UploadFile, File

from pydantic import BaseModel

import pandas as pd

import joblib

import io


# Create FastAPI app
app = FastAPI()


# Load trained model
model = joblib.load("../Models/rf_ltv_model.pkl")


# Input schema
class CustomerData(BaseModel):

    tenure: int

    MonthlyCharges: float


# Home route
@app.get("/")

def home():

    return {

        "message": "LTV Prediction API Running"

    }


# Single customer prediction
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


# Batch prediction endpoint
@app.post("/batch_predict")

async def batch_predict(

    file: UploadFile = File(...)
):

    contents = await file.read()

    df = pd.read_csv(

        io.StringIO(

            contents.decode('utf-8')
        )
    )

    predictions = model.predict(df)

    df['PredictedLTV'] = predictions

    return df.to_dict(

        orient='records'
    )