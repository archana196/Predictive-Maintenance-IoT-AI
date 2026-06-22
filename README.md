# Infotact Bangalore Internship – Project 1

# Manufacturing & Automotive Contextual Predictive Maintenance (IoT Edge AI)

## Internship Details

| Field                   | Details                                                                    |
| ----------------------- | -------------------------------------------------------------------------- |
| Internship Organization | Infotact Bangalore                                                         |
| Internship Domain       | Artificial Intelligence & Machine Learning                                 |
| Project Title           | Manufacturing & Automotive Contextual Predictive Maintenance (IoT Edge AI) |
| Project Duration        | Internship Project – Phase 1                                               |
| Team Type               | Collaborative Team Project                                                 |
| Technology Stack        | Python, Pandas, NumPy, Scikit-Learn, Jupyter Notebook, Git, GitHub         |
| Dataset                 | AI4I 2020 Predictive Maintenance Dataset                                   |

---

## Project Abstract

Predictive maintenance is a critical application of Artificial Intelligence in modern manufacturing and automotive industries. Unexpected equipment failures can lead to significant downtime, increased maintenance costs, production losses, and safety risks.

This project aims to develop an AI-powered Predictive Maintenance System capable of identifying potential machine failures before they occur by analyzing machine telemetry data and contextual environmental information.

The system combines Industrial IoT sensor measurements with contextual variables such as ambient temperature, load density, humidity, work shifts, and day type to create a more realistic industrial environment for predictive modeling.

The final objective is to build reliable machine learning models that can support proactive maintenance strategies, improve operational efficiency, reduce downtime, and optimize maintenance planning.

---

## Problem Statement

Traditional maintenance approaches are generally classified into:

### Reactive Maintenance

* Maintenance is performed only after failure occurs.
* Results in costly downtime.
* Increases operational risk.

### Preventive Maintenance

* Maintenance is performed on a fixed schedule.
* May replace components unnecessarily.
* Increases maintenance cost.

### Predictive Maintenance

* Maintenance decisions are based on actual machine condition.
* Failures can be predicted before occurrence.
* Improves operational efficiency and equipment reliability.

This project focuses on implementing Predictive Maintenance using Artificial Intelligence and Industrial IoT data.

---

## Project Objectives

The major objectives of this project are:

* Analyze machine telemetry data.
* Perform data cleaning and validation.
* Generate contextual environmental datasets.
* Integrate telemetry and contextual information.
* Engineer meaningful predictive features.
* Perform exploratory and correlation analysis.
* Develop machine learning models for failure prediction.
* Evaluate model performance using Stratified Cross Validation.
* Support proactive maintenance decision-making.

---

## Business Impact

The proposed solution can help industries:

* Reduce unexpected equipment failures.
* Minimize machine downtime.
* Improve maintenance planning.
* Increase equipment lifespan.
* Optimize production efficiency.
* Reduce operational and maintenance costs.
* Enable data-driven maintenance decisions.

---

## Technology Stack

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Matplotlib
* Scikit-Learn

### Development Environment

* Jupyter Notebook
* Git
* GitHub

### Dataset Source

AI4I 2020 Predictive Maintenance Dataset

### Machine Learning Techniques

* Classification Models
* Feature Engineering
* Correlation Analysis
* Stratified K-Fold Cross Validation
* Model Evaluation

---

## Project Workflow

```text
Dataset Collection
        ↓
Data Cleaning & Validation
        ↓
Failure Analysis
        ↓
Timestamp Generation
        ↓
External Context Generation
        ↓
Contextual Data Fusion
        ↓
Dataset Validation
        ↓
Feature Engineering
        ↓
Correlation Analysis
        ↓
Model Development
        ↓
Stratified Cross Validation
        ↓
Performance Evaluation
        ↓
Predictive Maintenance System
```

---

## Dataset Information

Dataset: AI4I 2020 Predictive Maintenance Dataset

Source: UCI Machine Learning Repository

Total Records: 10,000

Total Features: 14

Target Variable:

* Machine Failure

Failure Categories:

* Tool Wear Failure (TWF)
* Heat Dissipation Failure (HDF)
* Power Failure (PWF)
* Overstrain Failure (OSF)
* Random Failure (RNF)


# Project Timeline and Progress Summary

## Week 1 – Data Preparation and Validation

### Dataset Collection

The AI4I 2020 Predictive Maintenance Dataset was selected as the primary dataset for the project. The dataset contains machine telemetry measurements and failure indicators collected from industrial equipment.

### Dataset Understanding

Initial analysis was performed to understand:

* Dataset dimensions
* Feature descriptions
* Target variables
* Failure categories
* Data quality characteristics

### Data Cleaning and Preprocessing

The following preprocessing tasks were completed:

* Dataset loading and inspection
* Missing value analysis
* Duplicate record detection
* Data type verification
* Dataset integrity assessment
* Feature selection

### Identifier Removal

The following non-predictive identifier columns were removed:

* UDI
* Product ID

These features were excluded because they do not contribute to machine failure prediction and may introduce noise into machine learning models.

### Data Quality Assessment

Validation checks included:

* Missing value detection
* Duplicate record analysis
* Data type validation
* Dataset consistency checks

Results:

* Missing Values: 0
* Duplicate Records: 0
* Invalid Data Types: 0

### Exploratory Analysis

Machine failure distributions were analyzed to understand:

* Class imbalance
* Failure occurrence frequency
* Failure category distributions

The following failure categories were investigated:

* Tool Wear Failure (TWF)
* Heat Dissipation Failure (HDF)
* Power Failure (PWF)
* Overstrain Failure (OSF)
* Random Failure (RNF)

### Week 1 Deliverables

* Cleaned Dataset
* Data Cleaning Notebook
* Failure Analysis Notebook
* Validation Notebook
* Data Quality Report
* Dataset Validation Report

---

## Week 2 – Contextual Data Integration

### Timestamp Generation

A timestamp column was introduced into the AI4I dataset to enable contextual data fusion.

Generated Dataset:

```text
timestamps_added.csv
```

### External Context Dataset Generation

A synthetic contextual dataset was generated to simulate environmental and operational conditions.

Features Generated:

* Ambient Temperature
* Load Density
* Humidity
* Shift
* Day Type

Generated Dataset:

```text
external_context.csv
```

Rows Generated:

```text
10,000
```

### Contextual Data Fusion

The telemetry dataset and contextual dataset were integrated using timestamp-based alignment.

Merge Details:

* Merge Key: timestamp
* Merge Strategy: Left Join
* Telemetry Records: 10,000
* Context Records: 10,000

Generated Dataset:

```text
contextual_merged_dataset.csv
```

### Post-Merge Validation

Validation activities included:

* Row count verification
* Timestamp alignment checks
* Missing value analysis
* Duplicate record analysis
* Data type validation
* Dataset consistency validation

Validation Results:

* Missing Values: 0
* Duplicate Records: 0
* Data Type Issues: 0

### Dataset Quality Review

The merged dataset underwent a comprehensive quality assessment.

Checks Performed:

* Dataset completeness
* Feature availability
* Context feature consistency
* Dataset integrity
* Distribution review

Outcome:

The contextual dataset successfully passed all quality validation checks.

### Contextual Feature Engineering

Additional contextual insights were derived from the merged dataset.

Engineered Features:

#### Temperature Difference

```text
Temperature Difference =
Process Temperature - Ambient Temperature
```

Purpose:

Measures thermal stress and operating temperature variation.

#### Load Ratio

```text
Load Ratio =
Current Load / Maximum Load
```

Purpose:

Captures relative machine workload intensity.

#### Shift Encoding

Converts categorical shift information into machine learning compatible numerical values.

#### Day Type Encoding

Represents weekday and weekend operating conditions.

### Correlation Analysis

Correlation analysis was performed to study relationships between:

* Machine telemetry features
* Environmental factors
* Operational variables
* Failure indicators

Key Findings:

* Temperature variables exhibit positive relationships.
* Load Density influences machine operational characteristics.
* Tool Wear contributes significantly to failure patterns.
* Contextual variables provide additional predictive signals.

### Week 2 Deliverables

* Timestamp Enhanced Dataset
* External Context Dataset
* Merged Contextual Dataset
* Context Data Validation Notebook
* Dataset Quality Review Report
* Week 2 Validation Summary
* Updated Documentation

---

## Week 3 – Model Development Preparation

### Cross Validation Research

Research was conducted on:

* K-Fold Cross Validation
* Stratified K-Fold Cross Validation
* Handling Imbalanced Datasets
* Model Evaluation Strategies

### Stratified K-Fold Setup

A sample implementation was prepared using:

```python
from sklearn.model_selection import StratifiedKFold
```

Objectives:

* Preserve class distribution across folds
* Improve model evaluation reliability
* Handle machine failure class imbalance

Deliverables:

* stratified_cv_setup.ipynb
* stratified_cv_notes.md

### Upcoming Tasks

* Feature Engineering Optimization
* Machine Learning Model Development
* Random Forest Training
* XGBoost Training
* Model Comparison
* Ablation Study
* Performance Evaluation
* Explainable AI Analysis

---

# Final Project Status

## Completed

* Dataset Collection
* Dataset Cleaning
* Missing Value Analysis
* Duplicate Detection
* Data Type Validation
* Dataset Validation
* Failure Analysis
* Timestamp Generation
* External Context Generation
* Contextual Data Fusion
* Post-Merge Validation
* Dataset Quality Review
* Contextual Feature Engineering
* Correlation Analysis
* Documentation
* Cross Validation Research

## In Progress

* Model Development
* Feature Engineering Enhancement
* Stratified Cross Validation Setup
* Ablation Study
* Model Evaluation

## Expected Outcome

The final AI-powered Predictive Maintenance System will leverage machine telemetry and contextual environmental information to predict machine failures before they occur. The system aims to reduce downtime, optimize maintenance schedules, improve operational efficiency, and support data-driven maintenance decision-making in industrial environments.
