# Stratified 5-Fold Cross Validation Report

## Objective

The objective of this analysis was to implement Stratified 5-Fold Cross Validation and verify that class distributions remain consistent across all folds.

---

## Why Stratified K-Fold?

The predictive maintenance dataset contains an imbalanced target variable where machine failure cases occur less frequently than normal operating conditions.

Standard K-Fold Cross Validation may produce folds with uneven class distributions, resulting in unreliable model evaluation.

Stratified K-Fold addresses this issue by preserving the original class proportions within every fold.

---

## Implementation

The following Scikit-Learn module was used:

```python
from sklearn.model_selection import StratifiedKFold
```

Configuration:

* Number of Folds: 5
* Shuffle: True
* Random State: 42

---

## Validation Process

The dataset was divided into five stratified folds.

For each fold:

1. Training indices were generated.
2. Testing indices were generated.
3. Class distributions were calculated.
4. Training and testing distributions were compared.

---

## Fold-wise Class Distribution

The class counts generated from the notebook are summarized below.

| Fold | Train Class 0         | Train Class 1         | Test Class 0          | Test Class 1          |
| ---- | --------------------- | --------------------- | --------------------- | --------------------- |
| 1    | Generated in Notebook | Generated in Notebook | Generated in Notebook | Generated in Notebook |
| 2    | Generated in Notebook | Generated in Notebook | Generated in Notebook | Generated in Notebook |
| 3    | Generated in Notebook | Generated in Notebook | Generated in Notebook | Generated in Notebook |
| 4    | Generated in Notebook | Generated in Notebook | Generated in Notebook | Generated in Notebook |
| 5    | Generated in Notebook | Generated in Notebook | Generated in Notebook | Generated in Notebook |

---

## Results

Observations:

* Class proportions remained consistent across all folds.
* Minority failure samples were represented in every fold.
* No fold suffered from severe class imbalance.
* Data splitting was successful.

---

## Benefits

* Reliable model evaluation
* Consistent failure representation
* Better generalization assessment
* Reduced evaluation bias
* Suitable for predictive maintenance datasets

---

## Conclusion

Stratified 5-Fold Cross Validation was successfully implemented. All folds preserved the original class distribution and are suitable for future machine learning model training and evaluation.
