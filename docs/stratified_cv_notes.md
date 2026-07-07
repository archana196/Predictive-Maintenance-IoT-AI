# Stratified K-Fold Cross Validation Research

## Introduction

Cross Validation is a model evaluation technique used to estimate machine learning model performance on unseen data.

For predictive maintenance datasets, machine failures are usually rare events. This creates an imbalanced dataset where normal operating conditions greatly outnumber failure cases.

Because of this imbalance, Stratified K-Fold Cross Validation is preferred over standard K-Fold Cross Validation.

---

## Why Normal K-Fold is Unsuitable

Normal K-Fold randomly divides the dataset into K subsets.

Problems:

* Some folds may contain very few failure samples.
* Some folds may contain no failure samples.
* Evaluation metrics become unstable.
* Model performance may appear misleading.

For highly imbalanced datasets, normal K-Fold does not preserve class distribution.

---

## What is Stratified K-Fold?

Stratified K-Fold ensures that each fold maintains approximately the same class distribution as the original dataset.

Example:

Original Dataset:

* Normal Machines: 95%
* Failure Cases: 5%

Each fold will contain approximately the same ratio.

Benefits:

* Balanced evaluation
* Reliable performance metrics
* Better minority class representation
* Improved model assessment

---

## 5-Fold Stratified Cross Validation Workflow

### Step 1

Split the dataset into 5 stratified folds.

### Step 2

Use 4 folds for training.

### Step 3

Use the remaining fold for testing.

### Step 4

Repeat until every fold has served as the test set.

### Step 5

Average the evaluation results across all folds.

---

## Scikit-Learn Implementation

```python
from sklearn.model_selection import StratifiedKFold

skf = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)
```

---

## Application in This Project

The AI4I Predictive Maintenance dataset contains relatively few machine failure observations.

To ensure fair evaluation:

* 5-Fold Stratified Cross Validation will be used.
* Failure distribution will be preserved in every fold.
* Performance metrics will be averaged across folds.

---

## Conclusion

Stratified K-Fold Cross Validation is the preferred evaluation strategy for predictive maintenance datasets because it preserves class distribution across folds and provides more reliable model performance estimates for imbalanced classification problems.
