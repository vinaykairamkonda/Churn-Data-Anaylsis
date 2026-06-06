# Customer Churn Prediction & Lifetime Value (LTV) Engine

## Project Overview
Customer retention is one of the most critical challenges for subscription-based businesses and telecommunication companies. Acquiring a new customer is significantly more expensive than retaining an existing one.

This project develops an end-to-end Machine Learning and Analytics solution that:

* Predicts customers likely to churn.
* Estimates Customer Lifetime Value (LTV).
* Segments customers based on business value.
* Provides interactive dashboards for decision-making.
* Supports data-driven retention strategies.

The system combines Machine Learning, FastAPI, PostgreSQL, and Power BI to create a complete business intelligence solution.

---

# Business Problem
Telecommunication companies face customer attrition due to:
* High competition
* Pricing issues
* Service dissatisfaction
* Contract flexibility

The objective is to:

1. Predict customer churn before it occurs.
2. Identify key churn drivers.
3. Estimate future customer revenue.
4. Prioritize high-value customer retention campaigns.

---

# Dataset
### Dataset Used
IBM Telco Customer Churn Dataset
### Dataset Characteristics
* 7,043 Customers
* Customer Demographics
* Contract Information
* Internet Services
* Billing Information
* Payment Methods
* Customer Tenure
* Monthly Charges
* Total Charges
* Churn Status

---

# Tech Stack
## Programming
* Python
* SQL
  
## Data Processing
* Pandas
* NumPy

## Visualization
* Matplotlib
* Seaborn
* Power BI

## Machine Learning
* Scikit-Learn
* XGBoost
* SHAP

## API Development
* FastAPI

## Database
* PostgreSQL

## Version Control
* Git
* GitHub

---

# Project Workflow

## Week 1: Data Ingestion & Exploratory Data Analysis (EDA)
### Day 1-2
Database Setup

* Configured PostgreSQL database
* Loaded Telco Customer Churn dataset
* Verified data integrity

### Day 3-5
Exploratory Data Analysis

Analyzed:
* Contract Types
* Customer Tenure
* Monthly Charges
* Internet Services
* Payment Methods
* Churn Distribution

Created Visualizations:
* Churn Distribution
* Contract vs Churn
* Internet Service vs Churn
* Payment Method vs Churn
* Monthly Charges Distribution
* Tenure Analysis

### Day 6-7
Data Cleaning & Preparation

Performed:
* Missing Value Handling
* Data Type Corrections
* Outlier Analysis
* Categorical Encoding
* Baseline Analytics Report

---

# Week 2: Feature Engineering & Predictive Modeling

## Feature Engineering
Created advanced business features:

### AvgChargePerMonth
Customer spending trend.

### TotalServices
Total subscribed services.

### CustomerValueScore
Overall customer importance score.

### ContractRisk
Risk level based on contract type.

### AutoPayment
Whether automatic payment is enabled.

### FiberOpticUser
Fiber Optic service indicator.

### SeniorHighChargeRisk
High-risk senior customer group.

---

## Machine Learning Models

### Logistic Regression
Used as baseline classification model.

### Random Forest Classifier
Improved predictive performance.

### XGBoost Classifier
Best performing churn prediction model.

---

## Model Evaluation

Evaluated using:
* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC Score

---

## SHAP Explainability

Implemented SHAP to explain:
* Feature Importance
* Individual Customer Predictions
* Business Risk Drivers

Top Churn Drivers:
* Contract Type
* Monthly Charges
* Tenure
* Internet Service
* Payment Method

---

# Week 3: Customer Lifetime Value (LTV) & API Development

## LTV Prediction

Developed regression models to estimate:
* Expected Customer Revenue
* Future Business Value
* Revenue Contribution

Generated:
* Predicted LTV
* Customer Revenue Segments

### LTV Segments
* High LTV
* Medium LTV
* Low LTV

---

## FastAPI Development
Built FastAPI application for:

### Single Customer Prediction
Predict churn probability for one customer.

### Batch Prediction
Predict churn for multiple customers.

### LTV Prediction Endpoint
Estimate customer lifetime value.

---

## API Features

* Swagger UI Documentation
* Real-Time Inference
* JSON Responses
* Production Ready Structure

---

# Week 4: Visualization & Deployment

## Day 1-3
Power BI Integration
Connected processed datasets to Power BI.
Created business intelligence dashboards.

---

# Customer Churn Dashboard

## KPIs
* Total Customers: 7043
* Churned Customers: 1869
* Churn Rate: 26.54%
* Average Monthly Charge

## Visualizations

### Churn Distribution
Customer churn breakdown.

### Churn by Contract Type
Impact of contracts on churn.

### Churn by Internet Service
Internet service churn analysis.

### Churn by Payment Method
Payment behavior insights.

### Tenure Group vs Churn
Customer loyalty trends.

---

# Customer Lifetime Value Dashboard

## KPIs
* Total Customers: 7K
* Average LTV: ₹2.28K
* Maximum LTV: ₹8.55K
* Total Predicted Revenue: ₹16.06M
  
## Visualizations

### Customer Count by LTV Segment
Customer segmentation.

### Revenue by LTV Segment
Revenue contribution analysis.

### Average LTV by Segment
Segment profitability.

### LTV Distribution
Customer value distribution.

---

# Executive Business Insights

## Churn Insights
* Churn Rate is 26.54%.
* Month-to-Month contracts exhibit highest churn.
* Electronic Check users show elevated churn.
* Long-tenure customers demonstrate strong retention.
* Fiber Optic users have higher churn probability.

## LTV Insights
* Total projected customer revenue exceeds ₹16M.
* Average customer lifetime value is ₹2.28K.
* High LTV customers generate maximum revenue.
* Low LTV customers represent the largest customer segment.
* Retaining High LTV customers maximizes profitability.

---

# Docker Deployment

Implemented containerization using:
* Docker
* Docker Compose

Services:
* FastAPI
* PostgreSQL

---

# Author
Vinay Kairamkonda

Customer Churn Prediction & Lifetime Value (LTV) Engine

Built using Python, Machine Learning, FastAPI, PostgreSQL, Docker, and Power BI.
