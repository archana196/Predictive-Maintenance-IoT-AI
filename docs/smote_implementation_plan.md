# What is SMOTE?
Synthetic Minority Over-sampling Technique - generates synthetic samples for minority class (Machine failure = 1).

# Why use SMOTE?
Dataset is highly imbalanced:
- No failure (0): 9661 samples
- Failure (1): 339 samples
SMOTE balances this so model learns both classes equally.

# Risk of Data Leakage
If SMOTE applied BEFORE train-test split, synthetic samples leak into test data giving fake high accuracy.

# Correct Usage
SMOTE must be applied ONLY inside cross-validation training folds — never on test data!

# Implementation Strategy
1. Split data into train/test (stratified)
2. Inside each CV fold apply SMOTE on training fold only
3. Train LightGBM on oversampled data
4. Evaluate on original test fold
5. Report Macro F1 score