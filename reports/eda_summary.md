# EDA Summary Report

## Project
Contextual Predictive Maintenance (IoT Edge AI)

## Dataset
AI4I Predictive Maintenance Dataset

---

## Dataset Overview

- Total Records: 10,000
- Total Features: 14
- Numerical Features: 12
- Categorical Features: 2 (Product ID, Type)
- Target Variable: Machine Failure

### Sensor Features
- Air Temperature [K]
- Process Temperature [K]
- Rotational Speed [rpm]
- Torque [Nm]
- Tool Wear [min]

---

## Data Quality Assessment

### Missing Values
No missing values were found in the dataset.

### Data Types
All columns contain appropriate data types for analysis and feature engineering.

### Duplicates
No significant duplicate records were identified during data validation.

---

## Failure Distribution Analysis

| Class | Count |
|---------|---------|
| No Failure (0) | 9,661 |
| Failure (1) | 339 |

### Failure Rate

Failure Rate = (339 / 10000) × 100

**Failure Rate: 3.39%**

### Observation

The dataset is highly imbalanced because failure cases represent only a small percentage of the total records. This imbalance should be considered during model training and evaluation.

---

## Statistical Analysis

Summary statistics were generated using descriptive analysis.

Key observations:

- Air temperature ranges from 295.3 K to 304.5 K.
- Process temperature ranges from 305.7 K to 313.8 K.
- Rotational speed ranges from 1168 rpm to 2886 rpm.
- Torque ranges from 3.8 Nm to 76.6 Nm.
- Tool wear ranges from 0 to 253 minutes.

---

## Correlation Analysis

A correlation heatmap was generated to understand relationships between numerical variables.

### Findings

- Air temperature and process temperature show a positive correlation.
- Failure-related indicators exhibit relationships with operational sensor values.
- Most sensor variables have low direct linear correlation with each other, indicating that multiple factors contribute to machine failures.

---

## Distribution Analysis

Histograms were generated for numerical features to understand data distributions.

### Findings

- Sensor measurements are generally well distributed.
- Tool wear shows a broad range of values across machine operations.
- Rotational speed and torque demonstrate operational variability across machines.

---

## Outlier Analysis

Boxplots were generated to identify potential outliers.

### Findings

- Torque contains several extreme values.
- Rotational speed includes high-value observations.
- These values may represent critical operating conditions and should not be removed without domain justification.

---

## Key EDA Findings

1. The dataset contains 10,000 machine records and 14 features.
2. No missing values were detected.
3. Data quality is suitable for machine learning applications.
4. Machine failure occurs in only 3.39% of records, indicating class imbalance.
5. Air temperature and process temperature are positively correlated.
6. Torque and rotational speed exhibit operational variability.
7. Outliers may represent abnormal machine behavior and potential failure conditions.

---

## Conclusion

The AI4I Predictive Maintenance Dataset was successfully explored and validated. The dataset contains high-quality machine telemetry information with no missing values and suitable feature distributions. Initial analysis identified class imbalance and operational variability, which will be addressed in future stages through feature engineering, contextual data fusion, and predictive modeling.
