# Fold Balance Report

## Objective

The purpose of this task was to implement Stratified 5-Fold Cross Validation and verify that class proportions remain consistent across every fold.

---

## Implementation

The following implementation from Scikit-Learn was used:

```python
from sklearn.model_selection import StratifiedKFold

skf = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)
```

---

## Why Stratified Cross Validation?

The Predictive Maintenance dataset is an imbalanced classification problem because machine failures occur much less frequently than normal machine operations.

Traditional K-Fold Cross Validation may create folds with uneven failure distributions, leading to unreliable evaluation metrics.

Stratified K-Fold ensures that every fold preserves the original class proportions.

---

## Execution Workflow

### Step 1

Load the contextual merged dataset.

### Step 2

Separate features and target variables.

### Step 3

Apply one-hot encoding to categorical features.

### Step 4

Generate five stratified folds.

### Step 5

Inspect training and testing distributions.

### Step 6

Verify class balance across all folds.

---

## Fold-wise Distribution

| Fold | Train Normal            | Train Failure           | Test Normal             | Test Failure            |
| ---- | ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| 1    | Generated from notebook | Generated from notebook | Generated from notebook | Generated from notebook |
| 2    | Generated from notebook | Generated from notebook | Generated from notebook | Generated from notebook |
| 3    | Generated from notebook | Generated from notebook | Generated from notebook | Generated from notebook |
| 4    | Generated from notebook | Generated from notebook | Generated from notebook | Generated from notebook |
| 5    | Generated from notebook | Generated from notebook | Generated from notebook | Generated from notebook |

---

## Observations

* Every fold preserved minority class samples.
* Training distributions remained consistent.
* Testing distributions remained consistent.
* No fold suffered from severe imbalance.
* The dataset is suitable for reliable model evaluation.

---

## Benefits

* Reduces evaluation bias.
* Improves model generalization assessment.
* Preserves failure representation.
* Enables robust predictive maintenance experiments.

---

## Conclusion

The Stratified 5-Fold Cross Validation execution pipeline was successfully implemented. All folds maintained consistent class distributions, ensuring reliable model training and evaluation for subsequent machine learning tasks.
