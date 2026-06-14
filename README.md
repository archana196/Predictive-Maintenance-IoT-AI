# Infotact Bangalore Internship – Project 1

# Manufacturing & Automotive Contextual Predictive Maintenance (IoT Edge AI)

## Project Overview

This project aims to develop an AI-powered Predictive Maintenance System for manufacturing and automotive environments using Industrial IoT sensor data. The primary objective is to predict machine failures before they occur, enabling proactive maintenance, reducing downtime, lowering operational costs, and improving equipment reliability.

---

## Dataset Information

**Dataset:** AI4I 2020 Predictive Maintenance Dataset

### Original Dataset Statistics

| Metric        | Value  |
| ------------- | ------ |
| Total Rows    | 10,000 |
| Total Columns | 14     |

### Features

* UDI
* Product ID
* Type
* Air Temperature [K]
* Process Temperature [K]
* Rotational Speed [rpm]
* Torque [Nm]
* Tool Wear [min]
* Machine Failure
* TWF (Tool Wear Failure)
* HDF (Heat Dissipation Failure)
* PWF (Power Failure)
* OSF (Overstrain Failure)
* RNF (Random Failure)

---

## Data Cleaning & Preprocessing

The dataset was thoroughly inspected and cleaned to ensure data quality before model development.

### Preprocessing Activities

* Dataset loading and inspection
* Dataset structure validation
* Missing value analysis
* Duplicate record detection
* Data type validation
* Removal of unnecessary identifier columns:

  * UDI
  * Product ID
* Cleaned dataset generation

### Processed Dataset Statistics

| Metric        | Value  |
| ------------- | ------ |
| Total Rows    | 10,000 |
| Total Columns | 12     |

---

## Data Quality Assessment

### Missing Value Analysis

* Missing Values Found: **0**
* Dataset Completeness: **100%**

### Duplicate Record Analysis

* Duplicate Records Found: **0**

### Data Type Validation

All features were validated successfully and contain consistent data types suitable for machine learning workflows.

### Dataset Integrity

The dataset passed all integrity and quality validation checks.

---

## Validation Results

A dedicated validation pipeline was implemented to verify dataset consistency and readiness for machine learning.

| Validation Check               | Status   |
| ------------------------------ | -------- |
| Dataset Loading                | ✅ Passed |
| Shape Verification             | ✅ Passed |
| Column Validation              | ✅ Passed |
| Missing Value Validation       | ✅ Passed |
| Duplicate Detection            | ✅ Passed |
| Data Type Validation           | ✅ Passed |
| Statistical Summary Validation | ✅ Passed |
| Target Variable Validation     | ✅ Passed |
| Failure Category Validation    | ✅ Passed |
| Dataset Integrity Check        | ✅ Passed |

### Validation Conclusion

The dataset successfully passed all validation checks and is ready for feature engineering, contextual data fusion, and machine learning model development.

---

## Exploratory Analysis

### Machine Failure Distribution Analysis

Performed class distribution analysis on the target variable to understand dataset imbalance and prepare for future modeling strategies.

### Failure Category Analysis

Validated the distribution of:

* TWF
* HDF
* PWF
* OSF
* RNF

This analysis provides insights into machine failure patterns and supports future predictive modeling.

---

## Repository Structure

```text
Data/
├── preprocessed_ai4i2020.csv

Notebook/
├── cleaning.ipynb
├── failure_analysis.ipynb
├── validation.ipynb

reports/
├── data_quality_report.md

README.md
```

---

## Deliverables Completed

### Datasets

* preprocessed_ai4i2020.csv

### Notebooks

* cleaning.ipynb
* failure_analysis.ipynb
* validation.ipynb

### Reports

* data_quality_report.md

---

## Current Project Status

### Completed

* Dataset Collection
* Dataset Cleaning
* Data Quality Assessment
* Missing Value Analysis
* Duplicate Record Analysis
* Data Type Validation
* Feature Selection
* Dataset Validation
* Machine Failure Distribution Analysis
* Data Quality Reporting
* Documentation

### Upcoming Tasks

* Feature Engineering
* Contextual Data Fusion
* External Data Integration
* Model Training
* Model Evaluation
* Noise Sensitivity Analysis
* Performance Optimization

---

## Team Contribution

### Ajay Verma

#### Responsibilities

* Data Cleaning
* Data Validation
* Missing Value Analysis
* Duplicate Detection
* Data Type Verification
* Feature Selection
* Dataset Preparation
* Machine Failure Distribution Analysis
* Data Quality Reporting
* Repository Documentation

---

## Expected Outcome

The final system will combine IoT telemetry and contextual environmental factors to predict potential machine failures before they occur, enabling proactive maintenance decisions and reducing operational downtime.
