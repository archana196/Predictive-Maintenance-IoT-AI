# Week 3: Cross Validation and SMOTE Workflow

## Overview

During Week 3, the project focused on establishing a robust machine learning evaluation pipeline for predictive maintenance. The AI4I dataset exhibits significant class imbalance, with machine failure events occurring much less frequently than normal operations. To address this challenge, the team implemented Stratified 5-Fold Cross Validation and SMOTE (Synthetic Minority Over-sampling Technique).

These methods ensure reliable model evaluation while improving the model's ability to learn from minority-class failure events.

---

# Dataset Class Distribution

Before applying any balancing technique, the dataset contained:

| Class          | Count |
| -------------- | ----: |
| No Failure (0) | 9,661 |
| Failure (1)    |   339 |

Total Records: 10,000

Failure events account for only **3.39%** of the dataset, confirming a highly imbalanced classification problem.

---

# Stratified K-Fold Cross Validation

## Purpose

Stratified K-Fold Cross Validation ensures that each fold preserves the original class distribution of the dataset.

This is particularly important for predictive maintenance because failure records are rare.

---

## Implementation

The project uses:

```python
from sklearn.model_selection import StratifiedKFold

skf = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)
```

The dataset is divided into five folds.

For each iteration:

1. Four folds are used for training.
2. One fold is used for validation.
3. Class proportions remain consistent across all folds.

---

## Fold Distribution

Training data distribution observed during cross validation:

| Fold | Non-Failure | Failure |
| ---- | ----------: | ------: |
| 1    |        7728 |     272 |
| 2    |        7729 |     271 |
| 3    |        7729 |     271 |
| 4    |        7729 |     271 |
| 5    |        7729 |     271 |

The results confirm that Stratified K-Fold successfully maintained class balance across all folds.

---

# SMOTE Workflow

## Purpose

SMOTE is used to address class imbalance by generating synthetic samples for the minority class.

Instead of duplicating existing failure records, SMOTE creates new synthetic examples based on neighboring minority-class observations.

---

## Implementation

The project uses:

```python
from imblearn.over_sampling import SMOTE

smote = SMOTE(random_state=42)
```

SMOTE is applied only to the training data within each fold.

Example:

Before SMOTE:

| Class | Count |
| ----- | ----: |
| 0     |  7728 |
| 1     |   272 |

After SMOTE:

| Class | Count |
| ----- | ----: |
| 0     |  7728 |
| 1     |  7728 |

The minority class becomes fully balanced with the majority class.

---

# Data Leakage Risks

## What is Data Leakage?

Data leakage occurs when information from validation data is unintentionally used during model training.

This leads to unrealistically high evaluation scores and poor real-world performance.

---

## Incorrect Workflow

```text
Dataset
   ↓
Apply SMOTE
   ↓
Cross Validation
   ↓
Model Training
```

Problem:

* Synthetic samples may contain information derived from validation records.
* Evaluation metrics become unreliable.

---

## Correct Workflow

```text
Cross Validation Split
          ↓
Training Fold
          ↓
Apply SMOTE
          ↓
Train Model
          ↓
Validate on Original Validation Fold
```

This workflow prevents information leakage and ensures fair model evaluation.

---

# Integrated Modeling Pipeline

The Week 3 modeling workflow follows these steps:

```text
Context Features Dataset
            ↓
Data Cleaning
            ↓
Feature Selection
            ↓
Target Selection
            ↓
Stratified 5-Fold Split
            ↓
Training Fold
            ↓
Apply SMOTE
            ↓
Balanced Training Data
            ↓
LightGBM Training
            ↓
Validation Fold Evaluation
            ↓
Repeat for All Folds
            ↓
Average Performance Metrics
```

---

# Model Evaluation Results

A LightGBM classifier was trained using the SMOTE-balanced training folds.

| Fold | Macro F1 Score |
| ---- | -------------: |
| 1    |         0.5060 |
| 2    |         0.5047 |
| 3    |         0.3190 |
| 4    |         0.5004 |
| 5    |         0.5684 |

### Average Macro F1 Score

**0.4797**

The results demonstrate that the cross-validation and SMOTE pipeline successfully trained the model while maintaining proper evaluation practices.

---

# Conclusion

Week 3 established the foundation for machine learning model development by implementing Stratified 5-Fold Cross Validation and SMOTE-based class balancing. The workflow successfully addressed dataset imbalance, prevented data leakage, and provided a reliable framework for future predictive maintenance experiments. This pipeline will be used in upcoming weeks for model optimization, comparison, and performance improvement.
