# Infotact Banglore Internshi Project 1
Manufacturing and Automotive Contextual Predictive Maintenance (IoT Edge AI)
# Infotact Bangalore Internship Project 1

## Manufacturing and Automotive Contextual Predictive Maintenance (IoT Edge AI)

### Project Overview

This project focuses on building an AI-powered Predictive Maintenance System for manufacturing and automotive environments using IoT sensor data. The objective is to predict machine failures before they occur, helping industries reduce downtime, maintenance costs, and equipment breakdowns.

---

## Dataset Information

**Dataset:** AI4I 2020 Predictive Maintenance Dataset

### Original Dataset

* Total Rows: **10,000**
* Total Columns: **14**

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
* TWF
* HDF
* PWF
* OSF
* RNF

---

## Data Cleaning and Preprocessing

The following preprocessing steps were performed:

### 1. Dataset Loading

* Loaded the AI4I 2020 dataset using Pandas.
* Inspected dataset structure and feature information.

### 2. Data Quality Assessment

* Checked dataset dimensions.
* Analyzed feature names and data types.
* Verified dataset consistency.

### 3. Missing Value Analysis

* Checked all columns for missing values.
* Result: **No missing values found.**

### 4. Duplicate Record Analysis

* Checked for duplicate records.
* Result: **No duplicate rows found.**

### 5. Feature Selection

Removed unnecessary identifier columns:

* UDI
* Product ID

Reason:

* These columns do not contribute to machine failure prediction.
* They are unique identifiers and may introduce noise into the model.

### 6. Cleaned Dataset Generation

After preprocessing:

* Rows: **10,000**
* Columns: **12**

The cleaned dataset was generated and saved for further machine learning tasks.

---

## Repository Structure

Data/
├── preprocessed_ai4i2020.csv

Notebook/
├── cleaning.ipynb

README.md

---

## Current Progress

Completed:

* Dataset Collection
* Dataset Loading
* Data Quality Assessment
* Missing Value Analysis
* Duplicate Record Analysis
* Feature Selection
* Cleaned Dataset Generation

In Progress:

* Feature Engineering
* Model Training
* Model Evaluation

---

## Technologies Used

* Python
* Pandas
* NumPy
* Jupyter Notebook
* Git
* GitHub

---

## Team Contribution

### Ajay Verma

Responsible for:

* Data Cleaning
* Data Validation
* Missing Value Analysis
* Duplicate Detection
* Feature Selection
* Dataset Preparation
* Preprocessing Documentation

---

## Expected Outcome

The final system will predict potential machine failures using IoT sensor data and enable proactive maintenance decisions in manufacturing and automotive environments.
