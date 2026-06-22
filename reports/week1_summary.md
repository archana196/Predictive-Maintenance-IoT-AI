# Week 1 Final Summary

## Project

Contextual Predictive Maintenance (IoT Edge AI)

## Week 1 Objective

The objective of Week 1 was to ingest the AI4I Predictive Maintenance Dataset, perform exploratory data analysis, validate data quality, engineer rolling statistical features from machine telemetry signals, and establish a strong foundation for predictive maintenance modeling.

---

## Objectives Completed

### Dataset Ingestion

* Downloaded and loaded the AI4I Predictive Maintenance Dataset.
* Verified dataset structure, dimensions, and feature information.
* Inspected data types and dataset characteristics.

### Exploratory Data Analysis (EDA)

* Analyzed dataset statistics using descriptive analysis.
* Examined machine failure distribution.
* Generated histograms and boxplots for sensor variables.
* Performed correlation analysis using a heatmap.
* Identified class imbalance in the target variable.

### Data Quality Validation

* Checked for missing values.
* Verified duplicate records.
* Validated data types and dataset consistency.

### Signal Processing & Feature Engineering

* Generated rolling mean features.
* Generated rolling standard deviation features.
* Generated rolling variance features.
* Applied rolling windows of 5 and 10 observations.
* Created an engineered dataset containing baseline telemetry features.

### Documentation & Project Management

* Updated project README.
* Created dataset overview documentation.
* Created data dictionary.
* Maintained GitHub issues and project board tracking.

---

## Team Contributions

### Archana V

* Dataset ingestion and loading.
* Dataset inspection and validation.
* Exploratory Data Analysis.
* Failure distribution analysis.
* Correlation analysis.
* Team coordination and GitHub project management.

### AjayVerma

* Missing value analysis.
* Duplicate record verification.
* Data type validation.
* Data quality assessment.

### AbhaySoni

* Rolling mean feature generation.
* Rolling standard deviation feature generation.
* Rolling variance feature generation.
* Creation of `week1_features.csv`.

### Arundhati K

* README documentation.
* Dataset overview preparation.
* Data dictionary creation.
* Week 1 documentation support.

---

## Key Findings

* Dataset contains 10,000 machine records and 14 original features.
* No missing values were detected.
* No major data quality issues were identified.
* Machine failure rate is approximately 3.39%, indicating class imbalance.
* Rolling statistical features successfully captured short-term signal behavior.
* Feature engineering expanded the dataset from 14 features to 44 features.

---

## Week 1 Deliverables

Completed:

* Dataset Overview
* Data Dictionary
* EDA Notebook
* Data Cleaning Notebook
* Feature Engineering Notebook
* Engineered Dataset (`week1_features.csv`)
* README Documentation
* Week 1 Reports

---

## Week 2 Plan

### Contextual Data Fusion

* Generate synthetic weather dataset.
* Generate factory load dataset.
* Generate traffic density dataset.

### Data Integration

* Merge contextual datasets with machine telemetry data.
* Validate merged dataset integrity.

### Feature Engineering

* Create contextual features such as:

  * Temperature Difference
  * Load Ratio
  * Humidity Impact
  * Traffic Impact

### Analysis

* Perform correlation analysis on contextual features.
* Conduct ablation study to compare model performance with and without contextual information.

---

## Week 1 Status

Week 1 objectives have been successfully completed. The project repository has been updated with documentation, notebooks, engineered features, and project tracking artifacts. The team is prepared to begin Week 2: Contextual Data Fusion and Advanced Feature Engineering.
