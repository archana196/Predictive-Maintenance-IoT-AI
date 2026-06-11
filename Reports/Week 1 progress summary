# Week 1 Progress Summary

## Project Title
**Manufacturing and Automotive Contextual Predictive Maintenance (IoT Edge AI)**

## Reporting Period
**Week 1**

## Team Member
**Abhay**

---

## 1. Introduction

The primary objective of Week 1 was to understand the AI4I 2020 Predictive Maintenance dataset, perform preliminary analysis, and engineer rolling statistical features that can improve machine failure prediction. The work focused on data exploration, signal processing, and feature generation using Python and Jupyter Notebook.

---

## 2. Dataset Understanding and Exploration

The AI4I 2020 Predictive Maintenance dataset was loaded into Jupyter Notebook for analysis. Initial exploration was conducted to understand the structure, quality, and characteristics of the data.

### Activities Performed

- Imported required Python libraries:
  - Pandas
  - NumPy
  - Matplotlib
  - Seaborn
- Loaded the dataset into a DataFrame.
- Examined dataset dimensions.
- Reviewed feature names and descriptions.
- Generated summary statistics for numerical variables.
- Checked data types of all columns.
- Verified dataset consistency.

### Findings

- Dataset contains approximately 10,000 machine operation records.
- Multiple sensor measurements are available.
- Failure-related target variables are included.
- No major data quality issues were observed.

---

## 3. Exploratory Data Analysis (EDA)

Exploratory Data Analysis was performed to gain insights into machine behavior and sensor trends.

### Analysis Conducted

#### Feature Distribution Analysis

The distribution of key sensor variables was examined:

- Air Temperature [K]
- Process Temperature [K]
- Rotational Speed [rpm]
- Torque [Nm]
- Tool Wear [min]

#### Statistical Analysis

Calculated:

- Mean
- Median
- Standard Deviation
- Minimum Values
- Maximum Values
- Quartiles

#### Correlation Analysis

Relationships among sensor measurements were investigated to identify patterns that may influence machine failures.

### Outcome

The analysis provided a clear understanding of machine operating conditions and sensor behavior, establishing a foundation for advanced feature engineering.

---

## 4. Data Visualization

Several visualizations were created to understand trends and variability in machine sensor readings.

### Visualizations Generated

#### Histogram Analysis

Used to observe data distributions for:

- Tool Wear [min]
- Air Temperature [K]
- Torque [Nm]

#### Trend Visualization

Created line plots to study:

- Sensor fluctuations over time
- Changes in machine operating conditions

#### Comparative Visualization

Compared raw sensor signals with processed signals to evaluate smoothing effectiveness.

### Outcome

Visual analysis revealed fluctuations and operational trends that may be useful for predictive maintenance modeling.

---

## 5. Rolling Feature Engineering

A major objective of Week 1 was to create rolling statistical features capable of capturing short-term machine behavior.

### Features Selected

Rolling calculations were applied to:

- Air Temperature [K]
- Process Temperature [K]
- Rotational Speed [rpm]
- Torque [Nm]
- Tool Wear [min]

### Window Sizes Used

- Window Size = 5
- Window Size = 10

### Engineered Features

For each sensor variable, the following features were generated:

#### Rolling Mean

- Captures local average behavior.
- Helps smooth short-term fluctuations.

#### Rolling Standard Deviation

- Measures variability within the rolling window.
- Identifies unstable machine behavior.

#### Rolling Variance

- Quantifies signal dispersion.
- Detects changes in operating conditions.

### Example Features Created

- AirTemp_RollMean_5
- AirTemp_RollStd_5
- AirTemp_RollVar_5
- Torque_RollMean_10
- Torque_RollStd_10
- Torque_RollVar_10

### Outcome

These engineered features provide additional contextual information that can improve predictive maintenance model performance.

---

## 6. Signal Processing and Noise Reduction

Basic signal processing techniques were applied to improve data quality and reveal hidden trends.

### Activities

- Applied rolling mean smoothing.
- Compared original and smoothed sensor signals.
- Visualized the impact of smoothing on sensor measurements.

### Benefits

- Reduced random noise.
- Highlighted long-term operational patterns.
- Improved interpretability of sensor readings.

### Outcome

The processed signals provide a clearer representation of machine behavior and can enhance future predictive modeling efforts.

---

## 7. Variability Assessment

To understand machine stability, variability metrics were evaluated.

### Analysis Conducted

- Variance calculations
- Standard deviation measurements
- Comparison of stable and fluctuating sensor signals

### Outcome

The analysis identified sensor variables exhibiting significant fluctuations, which may serve as indicators of machine degradation and potential failure.

---

## 8. Deliverables Completed

### Technical Deliverables

- Dataset exploration notebook
- Statistical analysis report
- Sensor distribution visualizations
- Rolling mean feature generation
- Rolling standard deviation feature generation
- Rolling variance feature generation
- Signal smoothing analysis
- Trend comparison visualizations

### Documentation Deliverables

- Dataset understanding notes
- Feature engineering documentation
- Week 1 progress summary

---

## 9. Challenges Encountered

- Understanding relationships between multiple sensor variables.
- Selecting appropriate rolling window sizes.
- Interpreting sensor fluctuations and variability patterns.
- Managing large numbers of generated features.

### Resolution

These challenges were addressed through iterative analysis, visualization, and validation of engineered features.

---

## 10. Skills and Tools Utilized

### Programming Language

- Python

### Libraries

- Pandas
- NumPy
- Matplotlib
- Seaborn

### Development Environment

- Jupyter Notebook
- GitHub

### Concepts Applied

- Exploratory Data Analysis (EDA)
- Feature Engineering
- Rolling Statistics
- Signal Processing
- Data Visualization
- Predictive Maintenance Analytics

---

## 11. Week 1 Outcome

Week 1 objectives were successfully completed. The dataset was explored, sensor behavior was analyzed, and multiple rolling statistical features were engineered. These newly created features provide meaningful information regarding machine operating conditions and will support the development of predictive maintenance models in upcoming project phases.

---

## 12. Plan for Week 2

- Advanced feature engineering
- Machine learning model preparation
- Feature selection and importance analysis
- Predictive maintenance model development
- Model evaluation and performance comparison
- Documentation updates

---

## Week 1 Status

**✅ Completed Successfully**
