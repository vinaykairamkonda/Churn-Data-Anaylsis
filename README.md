# Customer Churn Prediction & Analysis

## Project Overview
This project focuses on predicting customer churn using Machine Learning techniques on the Telco Customer Churn dataset.

The goal is to identify customers who are likely to leave the telecom service and provide business insights to improve customer retention.
---
## Dataset
Dataset Used:
- Telco Customer Churn Dataset

Features include:
- Customer demographics
- Contract details
- Internet services
- Billing information
- Customer tenure
- Churn status
---
## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- SHAP
- Jupyter Notebook
---
## Project Workflow
### Week 1
- Data Loading
- Exploratory Data Analysis (EDA)
- Data Cleaning
- Data Visualization

### Week 2
- Feature Engineering
- Logistic Regression
- Random Forest
- XGBoost
- Model Evaluation
- ROC-AUC Analysis
- Cross Validation
- Hyperparameter Tuning
- SHAP Explainability
---
## Feature Engineering
Created advanced features such as:
- AvgChargePerMonth
- TotalServices
- CustomerValueScore
- ContractRisk
- AutoPayment
- FiberOpticUser
- SeniorHighChargeRisk
---
## Models Used
- Logistic Regression
- Random Forest Classifier
- XGBoost Classifier
---
## Evaluation Metrics
Models were evaluated using:
- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC Score
---
## SHAP Explainability
Implemented SHAP values to explain:
- Important churn factors
- Customer risk drivers
- Business insights for stakeholders
---
## Key Insights
- Month-to-month contracts increase churn risk
- High monthly charges contribute to churn
- Long tenure reduces churn probability
- Tech support improves retention
- Fiber optic users show higher churn rates

## FastAPI Deployment

- Built FastAPI backend for LTV prediction
- Implemented real-time customer inference
- Tested API using Swagger UI
- Added prediction endpoint using Random Forest model
