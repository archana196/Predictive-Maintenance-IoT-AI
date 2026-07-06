# Manufacturing & Automotive Contextual Predictive Maintenance (IoT Edge AI)

> **AI/ML Internship Project -- Infotact Solutions, Bangalore**

## Internship Details

  -----------------------------------------------------------------------
  Field                               Details
  ----------------------------------- -----------------------------------
  Organization                        Infotact Solutions, Bangalore

  Domain                              AI & Machine Learning

  Project                             Manufacturing & Automotive
                                      Contextual Predictive Maintenance

  Dataset                             AI4I 2020 Predictive Maintenance
                                      Dataset
  -----------------------------------------------------------------------

## Project Overview

This project develops an AI-powered predictive maintenance system
capable of predicting machine failures using industrial machine
telemetry and contextual operational data. It includes preprocessing,
feature engineering, SMOTE, Stratified 5-Fold Cross Validation, LightGBM
model development, and Flask deployment.

## Problem Statement

Traditional maintenance causes downtime or unnecessary servicing. The
objective is to predict failures before they occur to improve
reliability and reduce operational cost.

## Objectives

-   Data cleaning and validation
-   Failure analysis
-   Contextual data integration
-   Feature engineering
-   LightGBM model development
-   Stratified Cross Validation
-   Flask deployment

## Technology Stack

Python, Pandas, NumPy, Matplotlib, Scikit-learn, LightGBM, Flask,
Joblib, Bootstrap, Git, GitHub.

## Project Workflow

Dataset → Cleaning → Validation → Context Generation → Feature
Engineering → SMOTE → Stratified CV → LightGBM → Flask Dashboard

## Folder Structure

``` text
Predictive-Maintenance-IoT-AI/
├── data/
├── notebook/
├── reports/
├── docs/
├── flask_app/
│   ├── app.py
│   ├── model/
│   │   ├── model.pkl
│   │   └── encoders.pkl
│   ├── templates/
│   ├── static/
│   └── requirements.txt
└── README.md
```

## Week 1 Progress

-   Dataset collection
-   Cleaning
-   Validation
-   Failure analysis
-   Data quality assessment

## Week 2 Progress

-   Timestamp generation
-   Context dataset generation
-   Data fusion
-   Feature engineering
-   Correlation analysis

## Week 3 Progress

-   Stratified K-Fold
-   SMOTE
-   Cross Validation
-   Fold analysis
-   Documentation

## Week 4 Progress

-   LightGBM model
-   Flask dashboard
-   Prediction interface
-   Bootstrap UI
-   Confidence score
-   Model integration

## LightGBM Model

Input Features: 1. Type 2. Air_temperature_K 3. Process_temperature_K 4.
Rotational_speed_rpm 5. Torque_Nm 6. Tool_wear_min 7.
Ambient_Temperature 8. Load_Density 9. Humidity 10. Shift 11. Day_Type

Output: - Healthy - Failure

## Flask Dashboard

-   Prediction form
-   Responsive UI
-   Model loading
-   Encoders integration
-   Prediction results
-   Confidence score

## Features

-   Data preprocessing
-   Feature engineering
-   Contextual IoT integration
-   SMOTE
-   Stratified CV
-   LightGBM
-   Flask deployment

## Installation

``` bash
git clone <repository-url>
cd Predictive-Maintenance-IoT-AI/flask_app
pip install -r requirements.txt
python app.py
```

## Usage

Fill in machine details and click **Predict Machine Health**.

## Team Members

  Name         Contribution
  ------------ -----------------------------------------
  Ajay Verma   Validation, Stratified CV, Flask
  Archana      Contextual Data & Model
  Abhay        Feature Engineering
  Arundhati    Documentation

## Current Status

### Completed

-   Data preprocessing
-   Context fusion
-   Feature engineering
-   Stratified CV
-   SMOTE
-   LightGBM
-   Flask Dashboard

### In Progress

-   SHAP
-   Hyperparameter tuning
-   Model comparison
-   Deployment

## Expected Outcome

An AI-powered predictive maintenance platform that reduces downtime and
improves maintenance planning using machine learning.
