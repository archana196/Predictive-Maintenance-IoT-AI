# Threshold Tuning Summary Report

## Project

**Predictive Maintenance using IoT and Artificial Intelligence**

---

# Objective

The objective of this experiment was to determine the optimal probability threshold for the LightGBM classifier. Rather than relying on the default threshold of 0.50, multiple threshold values were evaluated to identify the operating point that provides the best balance between Precision and Recall. This process aims to improve the model's effectiveness in detecting machine failures while minimizing unnecessary maintenance alerts.

---

# Background

LightGBM produces prediction probabilities instead of direct class labels. By default, instances with a predicted probability of 0.50 or higher are classified as machine failures.

However, predictive maintenance systems often require a customized decision threshold because:

- Missing an actual machine failure can lead to equipment damage and production downtime.
- Predicting too many failures increases maintenance costs and unnecessary inspections.

Threshold tuning enables the selection of a probability cutoff that aligns with the application's operational requirements.

---

# Methodology

The threshold tuning process consisted of the following steps:

1. Load the engineered feature dataset.
2. Split the dataset into training and testing subsets.
3. Apply SMOTE to balance the minority failure class.
4. Train a LightGBM classifier.
5. Generate prediction probabilities for the test dataset.
6. Evaluate multiple classification thresholds.
7. Compute Precision, Recall, and F1 Score for each threshold.
8. Compare the results and identify the threshold with the best performance.

---

# Thresholds Evaluated

The following probability thresholds were analyzed during the experiment:

| Threshold |
|-----------:|
| 0.30 |
| 0.40 |
| 0.50 |
| 0.60 |
| 0.70 |

Each threshold produced a different balance between false positives and false negatives.

---

# Performance Metrics

The following evaluation metrics were calculated for every threshold.

## Precision

Precision measures how many predicted machine failures were actual failures.

A higher Precision indicates fewer false alarms.

---

## Recall

Recall measures how many actual machine failures were successfully detected.

A higher Recall reduces the likelihood of missing critical failures.

---

## F1 Score

The F1 Score combines Precision and Recall into a single performance metric.

It provides a balanced evaluation when both false positives and false negatives are important.

---

# Threshold Analysis

The experimental results demonstrated that changing the classification threshold directly influences model performance.

### Lower Thresholds

- Detect more machine failures.
- Increase Recall.
- May generate additional false alarms.
- Reduce Precision.

### Higher Thresholds

- Produce fewer false maintenance alerts.
- Increase Precision.
- Miss more actual failures.
- Lower Recall.

The optimal threshold is selected by identifying the highest F1 Score, which represents the best compromise between Precision and Recall.

---

# Visualization

The threshold tuning notebook generated a performance visualization showing:

- Precision versus Threshold
- Recall versus Threshold
- F1 Score versus Threshold

This graph illustrates how each metric changes as the decision threshold increases, enabling a data-driven selection of the most suitable threshold.

---

# Observations

The analysis indicates that threshold selection has a significant impact on predictive maintenance performance.

Key observations include:

- Precision generally improves as the threshold increases.
- Recall generally decreases with higher thresholds.
- F1 Score reaches its highest value at the threshold that best balances Precision and Recall.
- The default threshold of 0.50 is not always the optimal choice for predictive maintenance applications.

---

# Deliverables

The threshold tuning experiment generated the following outputs:

- Trained LightGBM classification model
- Prediction probability scores
- Threshold evaluation results
- Precision, Recall, and F1 Score measurements
- Threshold tuning performance graph (`threshold_tuning.png`)
- Recommended probability threshold for deployment

---

# Repository Files

```
Predictive-Maintenance-IoT-AI/
│
├── notebooks/
│   └── threshold_tuning.ipynb
│
├── reports/
│   ├── threshold_summary.md
│   └── threshold_tuning.png
│
└── docs/
    └── threshold_tuning_guide.md
```

---

# Conclusion

Threshold tuning is an important optimization step for binary classification models used in predictive maintenance. Evaluating multiple probability thresholds allows the model to be adapted to operational requirements instead of relying on the default classification cutoff. By selecting the threshold that provides the best balance between Precision and Recall, the predictive maintenance system becomes more reliable, reducing missed failures while limiting unnecessary maintenance actions. This analysis supports informed decision-making and contributes to improved machine reliability and maintenance efficiency.
