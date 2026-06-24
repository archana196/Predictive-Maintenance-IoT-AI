# Class Distribution Report

## Dataset Summary

Total Samples: 10000

Non-Failure Samples: 9661

Failure Samples: 339

Failure Rate: 3.39%

## Observation

The dataset is highly imbalanced.

Machine failures represent only a small percentage of all observations.

A standard train-test split may produce biased results.

Therefore:

- Stratified K-Fold Cross Validation will be used.
- SMOTE will be applied inside the training folds.
- LightGBM will be trained in Week 3.

## Conclusion

The dataset has been prepared for imbalanced classification modeling.
