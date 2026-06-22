# Week 1 Final Report

## Project Title
**Manufacturing & Automotive Contextual Predictive Maintenance (IoT Edge AI)**

## Introduction

Predictive maintenance is a data-driven approach that helps industries identify potential machine failures before they occur, reducing downtime and maintenance costs. The objective of Week 1 was to establish a strong foundation for the project by understanding the AI4I 2020 Predictive Maintenance Dataset, validating data quality, performing exploratory data analysis, analyzing machine failure patterns, and creating engineered features that can improve predictive model performance.

During this phase, the team focused on data preparation, feature understanding, and documentation activities to ensure the dataset was ready for advanced analytics and machine learning tasks in the upcoming weeks.

---

## Project Overview

The Manufacturing & Automotive Contextual Predictive Maintenance (IoT Edge AI) project aims to develop a machine learning solution that predicts equipment failures before they occur. Using machine sensor data and contextual information, the system seeks to improve maintenance planning, reduce unexpected downtime, and enhance operational efficiency. The AI4I 2020 Predictive Maintenance Dataset serves as the primary data source for developing and evaluating predictive models.

## Project Objectives

The primary objective of this project is to develop a predictive maintenance solution capable of identifying potential machine failures before they occur. The Week 1 objectives included:

- Understanding the AI4I 2020 dataset.
- Validating dataset quality and consistency.
- Performing exploratory data analysis.
- Investigating machine failure patterns.
- Creating rolling statistical features.
- Establishing project documentation and repository structure.
  
## Dataset Overview

The AI4I 2020 Predictive Maintenance Dataset contains operational and sensor measurements collected from industrial machines.

### Dataset Statistics

| Metric | Value |
|----------|----------|
| Total Records | 10,000 |
| Original Features | 14 |
| Processed Features | 12 |
| Target Variable | Machine Failure |

### Key Features

| Feature | Description |
|----------|------------|
| Type | Product quality category |
| Air Temperature [K] | Ambient air temperature |
| Process Temperature [K] | Machine process temperature |
| Rotational Speed [rpm] | Machine rotational speed |
| Torque [Nm] | Applied torque |
| Tool Wear [min] | Tool usage duration |
| Machine Failure | Failure indicator |
| TWF | Tool Wear Failure |
| HDF | Heat Dissipation Failure |
| PWF | Power Failure |
| OSF | Overstrain Failure |
| RNF | Random Failure |

The target variable, **Machine Failure**, indicates whether a machine experienced a failure event under specific operating conditions.

---


## Data Quality Assessment

Data quality validation was performed to ensure the reliability and consistency of the dataset before conducting further analysis.

### Missing Value Analysis

All features were examined for missing values.

**Result:** No missing values were found.

### Duplicate Record Analysis

Duplicate records were checked across the dataset.

**Result:** No duplicate records were detected.

### Data Type Validation

All variables were reviewed and validated.

**Result:**
- Numerical variables correctly stored as numeric values.
- Categorical variables properly identified.
- Binary failure indicators correctly represented.

### Data Preprocessing

The following identifier columns were removed:

- UDI
- Product ID

These columns were excluded because they do not contribute to machine failure prediction.

### Summary

The dataset successfully passed all quality checks and is suitable for machine learning applications.

---

## Exploratory Data Analysis (EDA)

EDA was conducted to understand data distributions, identify trends, and uncover relationships among variables.

### Failure Distribution Analysis

| Class | Count |
|---------|---------|
| No Failure | 9,661 |
| Failure | 339 |

### Failure Rate

\[
\text{Failure Rate} = \frac{339}{10000} \times 100
\]

**Failure Rate = 3.39%**

### Observation

The dataset is highly imbalanced because machine failures occur in only a small percentage of observations. This imbalance should be considered during model development.

---

### Statistical Analysis

Key observations:

- Air Temperature ranges from approximately 295 K to 304 K.
- Process Temperature ranges from approximately 306 K to 314 K.
- Rotational Speed ranges from approximately 1168 rpm to 2886 rpm.
- Torque values vary significantly across operating conditions.
- Tool Wear ranges from 0 to over 250 minutes.

---

### Correlation Analysis

A correlation heatmap was generated to examine relationships between variables.

#### Findings

- Air Temperature and Process Temperature show positive correlation.
- Failure indicators exhibit relationships with machine operating conditions.
- Machine failures are influenced by multiple factors rather than a single sensor reading.

---

### Distribution Analysis

Histograms were generated to study feature distributions.

#### Findings

- Sensor measurements are generally well distributed.
- Rotational speed and torque demonstrate operational variability.
- Tool wear exhibits a broad range of operating conditions.

---

### Outlier Analysis

Boxplots were used to identify extreme observations.

#### Findings

- Torque contains several high-value observations.
- Rotational speed includes extreme operating conditions.
- These values were retained because they may represent critical machine behavior.

---

## Failure Analysis

The dataset contains five machine failure categories:

- Tool Wear Failure (TWF)
- Heat Dissipation Failure (HDF)
- Power Failure (PWF)
- Overstrain Failure (OSF)
- Random Failure (RNF)

### Analysis Summary

Failure events are relatively rare compared to normal machine operations. Variations in temperature, rotational speed, torque, and tool wear appear to influence failure occurrence. These findings support the development of predictive maintenance models capable of early failure detection.

---

## Feature Engineering

Feature engineering was performed to capture machine behavior beyond raw sensor measurements.

### Rolling Statistical Features

Rolling statistics were generated for:

- Air Temperature
- Process Temperature
- Rotational Speed
- Torque
- Tool Wear

### Features Created

- Rolling Mean
- Rolling Standard Deviation
- Rolling Variance

### Window Sizes

- 5 observations
- 10 observations

### Benefits

- Captures short-term machine behavior.
- Identifies operational fluctuations.
- Enhances predictive capability for machine learning models.
- Provides additional contextual information from sensor signals.

### Outcome

The engineered dataset contains additional features that improve representation of machine operating conditions and support future predictive maintenance modeling.

---

## Tools and Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- Git
- GitHub

These tools were used for data analysis, visualization, feature engineering, documentation, and project management.

## Team Contributions

### Archana
- Dataset loading and inspection
- Exploratory Data Analysis
- Failure distribution analysis
- Project coordination and repository management

### Ajay
- Missing value analysis
- Duplicate verification
- Data type validation
- Data quality reporting

### Abhay
- Rolling feature engineering
- Statistical feature generation
- Engineered dataset creation

### Arundhati
- Dataset overview preparation
- Data dictionary creation
- README documentation
- Repository documentation support

---

## Key Findings

1. The dataset contains 10,000 machine records.
2. No missing values were detected.
3. No duplicate records were found.
4. Data quality is suitable for machine learning applications.
5. Machine failure rate is approximately 3.39%.
6. The dataset exhibits class imbalance.
7. Air and process temperatures are positively correlated.
8. Machine failures are influenced by multiple operational factors.
9. Rolling statistical features successfully capture short-term machine behavior.
10. The engineered dataset provides additional predictive information for future models.

---

## Deliverables Completed

- AI4I Dataset Acquisition
- Dataset Overview Document
- Data Dictionary
- Data Quality Report
- EDA Summary Report
- Failure Analysis Notebook
- Feature Engineering Notebook
- Rolling Feature Dataset
- README Documentation
- Week 1 Summary Report

---

## Conclusion

Week 1 objectives were successfully completed. The AI4I 2020 Predictive Maintenance Dataset was thoroughly explored, validated, and enhanced through statistical feature engineering. Data quality assessments confirmed that the dataset is clean and reliable, while exploratory analysis provided valuable insights into machine operating conditions and failure behavior.

The generated rolling statistical features enrich the dataset and improve its suitability for predictive maintenance modeling. With a validated dataset, comprehensive documentation, and engineered features in place, the project is well prepared to proceed to Week 2 activities involving contextual data integration, advanced feature engineering, and machine learning model development.
