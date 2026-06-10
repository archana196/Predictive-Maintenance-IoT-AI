# Data Quality Report

## Project

Manufacturing & Automotive Contextual Predictive Maintenance (IoT Edge AI)

## Prepared By

Ajay Verma

## Dataset Information

Dataset: AI4I 2020 Predictive Maintenance Dataset

### Original Dataset Statistics

* Total Rows: 10,000
* Total Columns: 14

### Removed Columns

The following identifier columns were removed during preprocessing:

* UDI
* Product ID

Reason:
These columns are unique identifiers and do not contribute to machine failure prediction.

### Processed Dataset Statistics

* Total Rows: 10,000
* Total Columns: 12

---

## Missing Value Analysis

A comprehensive missing value assessment was performed on all columns.

### Result

| Column                  | Missing Values |
| ----------------------- | -------------- |
| Type                    | 0              |
| Air temperature [K]     | 0              |
| Process temperature [K] | 0              |
| Rotational speed [rpm]  | 0              |
| Torque [Nm]             | 0              |
| Tool wear [min]         | 0              |
| Machine failure         | 0              |
| TWF                     | 0              |
| HDF                     | 0              |
| PWF                     | 0              |
| OSF                     | 0              |
| RNF                     | 0              |

### Conclusion

No missing values were detected in the dataset.

---

## Duplicate Record Analysis

Duplicate records were checked across the entire dataset.

### Result

* Duplicate Records Found: 0

### Conclusion

No duplicate rows were detected.

---

## Data Type Validation

Data types were inspected to verify consistency and suitability for machine learning workflows.

### Validation Summary

* Type: Categorical Feature
* Air temperature [K]: Numerical
* Process temperature [K]: Numerical
* Rotational speed [rpm]: Numerical
* Torque [Nm]: Numerical
* Tool wear [min]: Numerical
* Machine failure: Binary Target Variable
* TWF: Binary Indicator
* HDF: Binary Indicator
* PWF: Binary Indicator
* OSF: Binary Indicator
* RNF: Binary Indicator

### Conclusion

All columns contain valid and consistent data types appropriate for predictive maintenance analysis.

---

## Data Quality Assessment Summary

| Quality Check              | Result          |
| -------------------------- | --------------- |
| Missing Values             | None Found      |
| Duplicate Records          | None Found      |
| Invalid Data Types         | None Found      |
| Identifier Columns Removed | UDI, Product ID |
| Dataset Ready for Modeling | Yes             |

---

## Final Conclusion

The dataset successfully passed all data quality checks. No missing values, duplicate records, or data type inconsistencies were identified. After removing unnecessary identifier columns, the dataset is ready for feature engineering, exploratory analysis, and machine learning model development.
