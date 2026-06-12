# Contextual Predictive Maintenance (IoT Edge AI)

## Branch: Archana Contribution

This branch contains my work for **Week 1: IoT Telemetry Ingestion and Signal Processing** in the Predictive Maintenance project.

---

## Project Overview

This project focuses on predicting machine failures using industrial IoT sensor data. The aim is to build a predictive maintenance system using data analysis, signal processing, and machine learning techniques.

---

## My Contributions (Archana)

### Dataset Ingestion
- Loaded AI4I Predictive Maintenance Dataset using Pandas
- Checked dataset shape, columns, and data types
- Verified data quality (no missing values)

### Exploratory Data Analysis (EDA)
- Performed statistical analysis using `describe()`
- Analyzed machine failure distribution
- Created histograms for sensor features
- Created boxplots to detect outliers
- Generated correlation heatmap

### Data Understanding
- Identified key sensor variables:
  - Air Temperature
  - Process Temperature
  - Rotational Speed
  - Torque
  - Tool Wear
- Observed strong class imbalance in target variable

### GitHub Work
- Created and maintained GitHub Project Board
- Added and tracked Week 1 issues
- Coordinated team progress

---

## Dataset Summary

- Total Records: 10,000
- Total Features: 14
- Target Variable: Machine Failure
- Failure Rate: 3.39%

---

## Key Insights

- Dataset is highly imbalanced
- No missing values found
- Sensor data shows operational variability
- Torque and tool wear are important indicators of machine condition

---

## Tools Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## Week 1 Status

- Dataset ingestion completed
- EDA completed
- GitHub tracking completed
- Feature engineering handled by team member (Abhay)

---

## Next Steps

- Contextual data generation (weather, factory load, traffic)
- Feature fusion with sensor data
- Advanced feature engineering (Week 2)
