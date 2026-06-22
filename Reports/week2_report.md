# Week 2 Completion Report

## Manufacturing and Automotive Contextual Predictive Maintenance (IoT Edge AI)

### Project Overview

The second phase of the Manufacturing and Automotive Contextual Predictive Maintenance project focused on enhancing the AI4I 2020 Predictive Maintenance Dataset by integrating contextual information and performing advanced feature engineering. While the original dataset contains machine operational parameters and failure indicators, it does not capture external environmental and operational conditions that may influence machine behavior.

To address this limitation, contextual variables such as ambient temperature, humidity, load density, shift information, and day type were created and integrated with the machine telemetry dataset. This enriched dataset provides a more comprehensive representation of machine operating conditions and supports the development of more accurate predictive maintenance models.

The primary goal of this phase was to prepare a robust dataset capable of supporting machine learning models that can predict failures before they occur.

---

# Objectives

The objectives of this phase were:

* Generate timestamps for machine telemetry records.
* Create contextual environmental and operational variables.
* Integrate contextual information with machine telemetry data.
* Research and implement advanced contextual feature engineering techniques.
* Validate the quality and consistency of the integrated dataset.
* Analyze relationships among features using correlation analysis.
* Prepare an ablation study framework for future model evaluation.
* Document all activities and deliverables.

---

# Contextual Data Integration

## Timestamp Generation

The AI4I dataset originally lacked temporal information. To simulate a real-world IoT monitoring environment, timestamps were generated for all machine records.

Activities performed:

* Created sequential timestamps.
* Simulated one machine reading per minute.
* Added temporal structure to the dataset.
* Enabled future time-series analysis.

Benefits:

* Supports temporal feature engineering.
* Enables lag feature creation.
* Facilitates trend analysis.
* Simulates real industrial monitoring systems.

---

## Creation of Contextual Features

Several contextual variables were generated to represent environmental and operational conditions that may affect machine performance.

### Ambient Temperature

Represents the environmental temperature surrounding the machine during operation.

Importance:

* Influences machine efficiency.
* May contribute to overheating conditions.
* Provides environmental context.

### Humidity

Represents moisture levels in the environment.

Importance:

* May influence equipment degradation.
* Can affect long-term machine reliability.
* Supports environmental condition analysis.

### Load Density

Represents operational workload intensity.

Importance:

* Indicates machine stress levels.
* Helps identify high-demand operating periods.
* Supports failure pattern analysis.

### Shift

Represents the operating shift.

Possible values:

* Morning
* Evening
* Night

Importance:

* Captures operational differences between shifts.
* Helps identify shift-specific trends.

### Day Type

Represents the type of day.

Possible values:

* Weekday
* Weekend
* Holiday

Importance:

* Reflects production schedule variations.
* Captures operational workload differences.

---

# Data Fusion Process

Data fusion combines machine telemetry information with contextual variables to create a unified dataset.

## Fusion Methodology

The following steps were performed:

1. Generated timestamps for machine records.
2. Created contextual variables corresponding to each timestamp.
3. Aligned both datasets using timestamps.
4. Merged machine and contextual datasets.
5. Verified row counts and consistency.

## Benefits of Data Fusion

* Creates a richer dataset.
* Improves feature availability.
* Supports contextual failure analysis.
* Enhances predictive maintenance capabilities.

## Output

Generated Dataset:

* merged_context_dataset.csv

This dataset serves as the foundation for future modeling activities.

---

# Advanced Feature Engineering

Advanced contextual features were created to improve machine learning performance.

## Shift Encoding

Converted shift categories into numerical values.

Example:

* Morning = 0
* Evening = 1
* Night = 2

## Day Type Encoding

Converted day classifications into numerical values.

Example:

* Weekday = 0
* Weekend = 1
* Holiday = 2

## Interaction Features

Interaction features were created to capture combined effects of multiple contextual variables.

Examples:

* Temperature × Load Density
* Humidity × Load Density
* Temperature × Humidity

## Lag Features

Lag features capture historical information from previous observations.

Examples:

* Ambient Temperature Lag-1
* Humidity Lag-1
* Load Density Lag-1

## Rolling Statistical Features

Rolling statistics were generated to identify trends and variability.

Examples:

* Rolling Mean
* Rolling Standard Deviation
* Rolling Maximum
* Rolling Minimum

These engineered features provide additional information that may improve predictive performance.

---

# Correlation Analysis

Correlation analysis was performed to investigate relationships among machine telemetry features, contextual variables, engineered features, and machine failure.

Activities completed:

* Numerical feature selection.
* Correlation matrix generation.
* Correlation heatmap creation.
* Feature relationship analysis.

## Key Findings

* Several contextual features showed meaningful relationships with operational variables.
* Engineered features captured additional patterns not visible in original features.
* Correlation analysis provided guidance for feature selection in future modeling stages.

Outputs:

* correlation_analysis.ipynb
* correlation_analysis.md
* heatmap.png

---

# Dataset Validation

The integrated dataset was thoroughly validated to ensure quality and consistency.

## Validation Checks

### Missing Values

All columns were checked for missing values.

Result:

* No critical missing values detected.

### Duplicate Records

Dataset records were inspected for duplicates.

Result:

* No significant duplicate records identified.

### Data Type Validation

All feature data types were reviewed.

Result:

* Data types matched expected formats.

### Dataset Consistency

Consistency between machine telemetry and contextual datasets was verified.

Result:

* Data fusion completed successfully without integrity issues.

---

# Ablation Study Planning

An ablation study framework was prepared to evaluate the contribution of contextual features.

## Model A

Uses only internal machine telemetry features.

Features include:

* Air Temperature
* Process Temperature
* Rotational Speed
* Torque
* Tool Wear

## Model B

Uses:

* Internal telemetry features
* Contextual variables
* Engineered contextual features

## Evaluation Metrics

The following metrics will be used:

* Accuracy
* Precision
* Recall
* F1 Score

Purpose:

* Measure the effectiveness of contextual information.
* Compare predictive performance.
* Evaluate feature importance.

---

# Team Contributions

| Team Member | Contribution                                            |
| ----------- | ------------------------------------------------------- |
| Archana     | Timestamp generation, data fusion, correlation analysis |
| Ajay        | Contextual dataset creation, validation activities      |
| Abhay       | Advanced feature engineering, ablation study planning   |
| Arundhati   | Documentation, reporting, README maintenance            |

---

# Conclusion

Week 2 successfully transformed the original AI4I dataset into a contextual predictive maintenance dataset by integrating environmental and operational information. Advanced feature engineering, validation, and correlation analysis activities established a strong foundation for machine learning model development.

The project now possesses a validated and enriched dataset capable of supporting predictive maintenance research and experimentation. Future work will focus on feature selection, model training, evaluation, and comparison of contextual and non-contextual predictive maintenance models.
