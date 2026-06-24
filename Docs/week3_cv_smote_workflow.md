# Week 3: Cross Validation and SMOTE Workflow Documentation

## Introduction

As the project transitions from data preparation to machine learning model development, it is important to establish a reliable evaluation framework and address class imbalance issues within the predictive maintenance dataset.

Machine failure events are relatively rare compared to normal machine operations. This creates an imbalanced classification problem that can negatively affect model performance. To overcome this challenge, Week 3 introduces two important techniques:

1. Stratified K-Fold Cross Validation
2. Synthetic Minority Over-sampling Technique (SMOTE)

These methods help ensure reliable model evaluation and improved failure detection capability.

---

# Stratified K-Fold Cross Validation Workflow

## What is Cross Validation?

Cross Validation is a model evaluation technique used to estimate how well a machine learning model will perform on unseen data.

Instead of using a single train-test split, the dataset is divided into multiple folds, allowing the model to be trained and validated several times.

This approach provides a more reliable estimate of model performance.

---

## Why Standard K-Fold is Not Enough

The predictive maintenance dataset contains significantly more normal machine records than failure records.

Example:

| Class      | Percentage |
| ---------- | ---------- |
| No Failure | 96%        |
| Failure    | 4%         |

In standard K-Fold Cross Validation, random splitting may produce folds with very different class distributions.

Possible issues:

* Some folds may contain very few failures.
* Some folds may contain no failures.
* Validation metrics become unstable.
* Performance estimates become misleading.

---

## What is Stratified K-Fold?

Stratified K-Fold ensures that each fold maintains approximately the same class distribution as the original dataset.

For example:

Original Dataset:

* 96% Non-Failure
* 4% Failure

Each fold will also contain approximately:

* 96% Non-Failure
* 4% Failure

This results in fairer and more consistent model evaluation.

---

## 5-Fold Stratified Workflow

Step 1:
Load dataset and define features (X) and target (y).

Step 2:
Initialize StratifiedKFold.

```python
from sklearn.model_selection import StratifiedKFold

skf = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)
```

Step 3:
Generate training and validation folds.

Step 4:
Train model on training fold.

Step 5:
Evaluate model on validation fold.

Step 6:
Repeat for all five folds.

Step 7:
Average performance metrics across folds.

---

# SMOTE Workflow

## What is SMOTE?

SMOTE (Synthetic Minority Over-sampling Technique) is an oversampling method designed to address class imbalance.

Instead of simply duplicating failure records, SMOTE creates new synthetic minority samples by interpolating between existing minority class observations.

This increases the number of machine failure examples available during training.

---

## Why SMOTE is Required

When a dataset is highly imbalanced, machine learning models tend to favor the majority class.

Consequences include:

* High accuracy
* Poor failure detection
* Low recall for machine failures

SMOTE helps balance the dataset and encourages the model to learn patterns associated with failures.

---

## SMOTE Implementation Workflow

Step 1:
Receive training fold from Stratified Cross Validation.

Step 2:
Apply SMOTE only to the training data.

```python
from imblearn.over_sampling import SMOTE

smote = SMOTE(random_state=42)

X_train_smote, y_train_smote = smote.fit_resample(
    X_train,
    y_train
)
```

Step 3:
Train machine learning model on balanced training data.

Step 4:
Evaluate on original validation data.

Step 5:
Repeat for all folds.

---

# Data Leakage Risks

## What is Data Leakage?

Data leakage occurs when information from the validation dataset becomes available during model training.

This causes unrealistically high performance scores and unreliable evaluation results.

---

## Incorrect SMOTE Usage

A common mistake is applying SMOTE before Cross Validation.

Incorrect Workflow:

```text
Full Dataset
      ↓
Apply SMOTE
      ↓
Cross Validation
      ↓
Train Model
```

Problem:

Synthetic samples generated from validation records may appear in training folds.

Result:

* Inflated accuracy
* Inflated F1 scores
* Unrealistic performance estimates

---

## Correct SMOTE Usage

Correct Workflow:

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

Benefits:

* No information leakage
* Reliable evaluation
* Realistic performance estimates

---

# Combined Week 3 Workflow

```text
Context Features Dataset
            ↓
Remove Identifier Columns
            ↓
Feature / Target Separation
            ↓
Class Distribution Analysis
            ↓
Stratified 5-Fold Split
            ↓
Training Fold
            ↓
Apply SMOTE
            ↓
Train Model
            ↓
Validate Model
            ↓
Repeat for All Folds
            ↓
Average Evaluation Metrics
```

---

# Expected Outcomes

By implementing Stratified K-Fold and SMOTE correctly, the project will achieve:

* Balanced training datasets
* Improved failure prediction capability
* Reliable validation results
* Reduced bias toward majority classes
* Better model generalization

These techniques establish a strong foundation for upcoming machine learning experiments using LightGBM and other predictive maintenance models.

---

# Conclusion

Week 3 focuses on preparing a robust machine learning workflow through proper validation and imbalance handling strategies. Stratified K-Fold ensures consistent evaluation across folds, while SMOTE addresses the scarcity of failure samples during training. Together, these methods improve the reliability and effectiveness of predictive maintenance model development.
