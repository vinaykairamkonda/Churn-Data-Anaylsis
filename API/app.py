from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel, Field

import pandas as pd
import joblib
import io


# Create FastAPI app
app = FastAPI(
    title="Customer Lifetime Value Prediction API",
    description="Predict customer lifetime value using machine learning",
    version="1.0.0"
)


# Load trained model
model = joblib.load("../Models/rf_ltv_model.pkl")


# Input schema with validation
class CustomerData(BaseModel):

    tenure: int = Field(
        gt=0,
        description="Customer tenure in months"
    )

    MonthlyCharges: float = Field(
        gt=0,
        description="Monthly charge amount"
    )


# Home endpoint
@app.get("/")
def home():

    return {
        "message": "LTV Prediction API Running"
    }


# Single customer prediction
@app.post("/predict")
def predict(data: CustomerData):

    input_data = pd.DataFrame([{
        "tenure": data.tenure,
        "MonthlyCharges": data.MonthlyCharges
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
            contents.decode("utf-8")
        )
    )

    predictions = model.predict(df)

    df["PredictedLTV"] = predictions

    return df.to_dict(
        orient="records"
    )