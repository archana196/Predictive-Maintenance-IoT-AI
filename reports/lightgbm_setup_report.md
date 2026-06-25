# LightGBM Baseline Model Report

## Objective

Train an initial LightGBM classifier for predictive maintenance.

## Dataset

* Source: context_features_dataset.csv
* Target Variable: Machine Failure

## Preprocessing

* Removed unnecessary columns
* Converted timestamp into numerical features
* Prepared feature matrix and target variable
* Performed train-test split

## Model

* LightGBM Classifier
* Random State: 42

## Results

Accuracy: [Paste your accuracy here]

### Classification Report

[Paste classification report output]

### Confusion Matrix

[Paste confusion matrix output]

## Observation

The baseline model trained successfully and provides an initial benchmark for future evaluation using Stratified K-Fold Cross Validation and SMOTE.

## Next Steps

* Implement Stratified 5-Fold Cross Validation
* Apply SMOTE within training folds
* Evaluate Precision, Recall, F1-Score, and ROC-AUC
