# Noise Sensitivity Analysis Report

## Overview

This report presents the results of the noise sensitivity analysis conducted on the Predictive Maintenance IoT-AI model. The objective of this experiment was to evaluate how the trained machine learning model performs when sensor data is affected by artificial noise. Since Industrial IoT environments often experience sensor inaccuracies, communication errors, and environmental interference, assessing model robustness under noisy conditions is essential.

---

# Objective

The primary objectives of the noise sensitivity analysis are:

- Evaluate the robustness of the predictive maintenance model.
- Measure the impact of noisy sensor readings on prediction performance.
- Compare evaluation metrics before and after adding noise.
- Identify potential weaknesses of the model in real-world deployment scenarios.

---

# Experimental Setup

The trained model was first evaluated using the original test dataset. Artificial noise was then introduced into the feature values to simulate unreliable sensor measurements. The same trained model was evaluated again without retraining.

The following performance metrics were used for comparison:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC

---

# Results

| Metric | Original Dataset | Noisy Dataset |
|---------|----------------:|--------------:|
| Accuracy | 0.9990 | 0.1435 |
| Precision | 1.0000 | 0.0371 |
| Recall | 0.9706 | 0.9706 |
| F1-Score | 0.9851 | 0.0715 |
| ROC-AUC | 0.9901 | 0.8139 |

---

# Performance Analysis

## Accuracy

The model achieved an excellent accuracy of **99.90%** on the original dataset. After introducing noise, the accuracy dropped dramatically to **14.35%**, indicating that noisy sensor values significantly affect overall prediction performance.

---

## Precision

Precision decreased from **100%** to **3.71%**. This substantial decline indicates that the model generated a large number of false positive predictions when operating on noisy data.

---

## Recall

Recall remained constant at approximately **97.06%** for both datasets. This suggests that the model continued detecting most machine failures even under noisy conditions.

---

## F1-Score

The F1-Score decreased from **0.9851** to **0.0715**. Since the F1-Score balances both precision and recall, this decline reflects the severe reduction in overall classification quality caused by noise.

---

## ROC-AUC

ROC-AUC reduced from **0.9901** to **0.8139**. Although still above random guessing, the decrease indicates that the model's ability to distinguish between machine failures and normal operations weakened considerably.

---

# Discussion

The experiment demonstrates that the predictive maintenance model performs exceptionally well when clean sensor data is available. However, the addition of artificial noise significantly reduces prediction quality.

The model continues to detect most machine failures (high recall), but it incorrectly classifies many healthy machines as failures, leading to poor precision and overall accuracy. This behavior suggests that the model is highly sensitive to noisy input features.

In practical Industrial IoT systems, noisy sensor readings can result from hardware degradation, electromagnetic interference, communication delays, or environmental conditions. Therefore, improving the model's robustness against noisy data is an important consideration before deployment.

---

# Recommendations

To improve performance under noisy conditions, the following enhancements are recommended:

- Apply sensor data filtering techniques before prediction.
- Use feature scaling and normalization consistently.
- Introduce noise-augmented samples during model training.
- Perform feature selection to remove unstable variables.
- Explore more robust ensemble learning algorithms.
- Implement anomaly detection to identify corrupted sensor readings before classification.

---

# Conclusion

The noise sensitivity analysis highlights the importance of data quality in predictive maintenance systems. While the trained model achieves outstanding performance on clean data, its effectiveness decreases substantially when exposed to noisy sensor measurements.

The results indicate that additional preprocessing and robustness-enhancing techniques are necessary to ensure reliable machine failure prediction in real-world Industrial IoT environments. Future work should focus on developing models that maintain stable performance despite fluctuations in sensor data quality.
