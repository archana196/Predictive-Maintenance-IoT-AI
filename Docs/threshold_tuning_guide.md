# Threshold Tuning Guide

## Overview

Threshold tuning is the process of selecting the optimal probability cutoff for converting predicted probabilities into class labels. By default, most binary classification models use a threshold of **0.50**, meaning any prediction with a probability greater than or equal to 0.50 is classified as a positive instance.

For predictive maintenance, using the default threshold is not always ideal. Missing a machine failure (false negative) can be much more expensive than generating an unnecessary maintenance alert (false positive). Threshold tuning helps balance these trade-offs.

---

## Objectives

The primary objectives of threshold tuning are:

- Improve overall model performance.
- Find the threshold that maximizes the F1 Score.
- Analyze the trade-off between Precision and Recall.
- Select a threshold suitable for predictive maintenance applications.
- Reduce missed machine failures while controlling false alarms.

---

## Why Threshold Tuning?

Machine learning classifiers such as LightGBM output probabilities rather than direct class labels.

For example:

| Predicted Probability | Default Prediction (0.50) |
|----------------------:|--------------------------:|
| 0.28 | 0 |
| 0.42 | 0 |
| 0.57 | 1 |
| 0.81 | 1 |

Changing the threshold changes the classification decision.

Example:

Threshold = **0.30**

| Probability | Prediction |
|------------:|-----------:|
| 0.28 | 0 |
| 0.42 | 1 |
| 0.57 | 1 |
| 0.81 | 1 |

Threshold = **0.70**

| Probability | Prediction |
|------------:|-----------:|
| 0.28 | 0 |
| 0.42 | 0 |
| 0.57 | 0 |
| 0.81 | 1 |

Lower thresholds increase Recall, while higher thresholds generally increase Precision.

---

# Workflow

```
Load Dataset
      │
      ▼
Train LightGBM Model
      │
      ▼
Generate Prediction Probabilities
      │
      ▼
Test Multiple Threshold Values
      │
      ▼
Calculate Precision
Calculate Recall
Calculate F1 Score
      │
      ▼
Compare Results
      │
      ▼
Select Best Threshold
```

---

## Implementation Steps

### Step 1 – Load Dataset

- Read the engineered feature dataset.
- Separate predictor variables and target labels.
- Split the dataset into training and testing sets.

---

### Step 2 – Handle Class Imbalance

Apply SMOTE to the training data to balance the minority class before model training.

Benefits include:

- Better learning of failure patterns.
- Reduced prediction bias.
- Improved Recall.

---

### Step 3 – Train the Model

Train a LightGBM classifier using the balanced dataset.

Model outputs predicted probabilities ranging from 0 to 1 for each machine instance.

---

### Step 4 – Generate Prediction Probabilities

Instead of predicting class labels directly, use the model to generate probabilities.

Example:

| Sample | Probability |
|-------:|------------:|
| 1 | 0.17 |
| 2 | 0.63 |
| 3 | 0.81 |
| 4 | 0.42 |

---

### Step 5 – Evaluate Different Thresholds

Test multiple threshold values such as:

| Threshold |
|-----------|
| 0.30 |
| 0.40 |
| 0.50 |
| 0.60 |
| 0.70 |

For each threshold:

- Convert probabilities into class labels.
- Compute Precision.
- Compute Recall.
- Compute F1 Score.

---

## Performance Metrics

### Precision

Measures the proportion of predicted failures that are actual failures.

**Formula**

```
Precision = TP / (TP + FP)
```

Higher Precision means fewer false maintenance alerts.

---

### Recall

Measures the proportion of actual failures detected by the model.

**Formula**

```
Recall = TP / (TP + FN)
```

Higher Recall reduces missed machine failures.

---

### F1 Score

The harmonic mean of Precision and Recall.

**Formula**

```
F1 = 2 × (Precision × Recall)
     ------------------------
      Precision + Recall
```

The threshold with the highest F1 Score is typically chosen as the optimal operating point.

---

## Threshold Analysis

As the threshold changes:

- Precision generally increases with higher thresholds.
- Recall generally decreases with higher thresholds.
- F1 Score often peaks at an intermediate threshold.

This analysis helps identify the threshold that provides the best balance between detecting failures and minimizing false alarms.

---

## Visualization

The notebook generates a Threshold Tuning Analysis graph showing:

- Precision vs Threshold
- Recall vs Threshold
- F1 Score vs Threshold

This visualization illustrates how model performance changes as the decision threshold varies and supports selecting an appropriate operating threshold.

---

## Outputs

The notebook produces:

- Trained LightGBM model
- Prediction probabilities
- Threshold evaluation table
- Precision, Recall, and F1 Score for each threshold
- Threshold tuning visualization (`threshold_tuning.png`)
- Optimal threshold based on F1 Score

---

## Repository Files

```
docs/
└── threshold_tuning_guide.md

notebooks/
└── threshold_tuning.ipynb

reports/
└── threshold_tuning.png
```

---

## Conclusion

Threshold tuning is an essential step in optimizing binary classification models for predictive maintenance. Instead of relying on the default decision threshold, evaluating multiple threshold values enables a better balance between Precision and Recall. Selecting the threshold with the highest F1 Score improves the reliability of failure detection and supports more effective maintenance planning by reducing both missed failures and unnecessary maintenance actions.
