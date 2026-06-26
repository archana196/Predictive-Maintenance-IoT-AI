

# Predictive Maintenance using IoT & AI

## Project Overview

This repository contains my contributions to the Predictive Maintenance using IoT & AI project. The objective is to develop a machine learning model capable of predicting machine failures by combining industrial sensor data with simulated contextual information.

---

## Contributions

### Dataset Preparation

* Uploaded and organized the AI4I 2020 Predictive Maintenance dataset.
* Explored the dataset and identified the target variable and input features.
* Removed unnecessary identifier columns for modeling.
* Analyzed class imbalance in the dataset.

### Contextual Data Integration

* Simulated timestamp values for every machine record.
* Designed the structure of the external contextual dataset.
* Merged machine sensor data with contextual information using timestamps.
* Validated merged data and resolved timestamp inconsistencies.

### Feature Engineering

* Created contextual features including:

  * Temperature Difference (`temp_diff`)
  * Load Ratio (`load_ratio`)
  * Humidity Impact (`humidity_impact`)
* Performed correlation analysis on engineered features.
* Prepared the final modeling dataset.

### Machine Learning Preparation

* Prepared feature (`X`) and target (`y`) datasets.
* Verified class imbalance before model training.
* Initialized the LightGBM training workflow.
* Generated baseline model evaluation metrics.

### Project Coordination

* Created and managed GitHub Issues.
* Updated the project board.
* Coordinated task distribution among team members.
* Maintained project documentation.

---

## Repository Structure

```text
data/
├── ai4i2020.csv
├── timestamps_added.csv
├── external_context.csv
├── context_features_dataset.csv
├── model_ready_dataset.csv

notebooks/
├── timestamp_creation.ipynb
├── context_merge.ipynb
├── feature_engineering.ipynb
├── week3_modeling_setup.ipynb
├── lightgbm_training.ipynb

reports/
├── class_distribution.md
├── week3_dataset_summary.md
├── lightgbm_setup_report.md

docs/
├── context_overview.md
├── project_notes.md
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* LightGBM
* Matplotlib
* Git & GitHub
* Jupyter Notebook

---

## Current Progress

* ✅ Dataset preparation completed
* ✅ Contextual data integration completed
* ✅ Feature engineering completed
* ✅ Baseline LightGBM model implemented
* 🔄 Stratified Cross Validation and SMOTE integration in progress

---

## Future Work

* Implement Stratified 5-Fold Cross Validation
* Integrate SMOTE within training folds
* Compare baseline and balanced models
* Evaluate Precision, Recall, F1-Score, ROC-AUC
* Finalize project documentation and results

