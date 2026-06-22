# Class Distribution Report

## Objective

Prepare the contextual predictive maintenance dataset for machine learning modeling.

## Dataset Preparation

Completed the following tasks:

* Loaded context_features_dataset.csv
* Identified target variable (Machine failure)
* Identified feature columns
* Removed non-informative identifier columns:

  * UDI
  * Product ID
* Verified dataset structure and data types
* Checked for missing values

## Class Distribution Analysis

Target Variable:

Machine failure

* 0 = Normal Operation
* 1 = Machine Failure

The dataset shows class imbalance, with failure records representing only a small percentage of total observations.

## Observation

An imbalanced dataset can cause machine learning models to favor the majority class and under-detect machine failures.

## Next Steps

* Train/Test Split
* Apply SMOTE
* Train LightGBM Model
* Evaluate using Accuracy, Precision, Recall, F1-Score, and ROC-AUC
