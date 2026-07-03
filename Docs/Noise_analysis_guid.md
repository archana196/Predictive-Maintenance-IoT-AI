# Noise Sensitivity Analysis Summary

## Objective

The objective of this analysis is to evaluate the robustness of the predictive maintenance model by measuring its performance on the original dataset and comparing it with performance after introducing artificial noise. This experiment helps determine how well the model can handle noisy sensor data commonly encountered in Industrial IoT environments.

---

## Methodology

The following steps were performed during the analysis:

1. The trained predictive maintenance model was evaluated using the original test dataset.
2. Artificial noise was introduced into the input features to simulate faulty or unstable sensor readings.
3. The same trained model was evaluated on the noisy dataset.
4. Performance metrics from both evaluations were compared to measure the model's sensitivity to noise.

---

## Performance Comparison

| Metric | Original Dataset | Noisy Dataset |
|---------|----------------:|--------------:|
| Accuracy | 0.9990 | 0.1435 |
| Precision | 1.0000 | 0.0371 |
| Recall | 0.9706 | 0.9706 |
| F1-Score | 0.9851 | 0.0715 |
| ROC-AUC | 0.9901 | 0.8139 |

---

## Analysis

The model demonstrates outstanding performance on the original dataset, achieving nearly perfect classification results across all evaluation metrics.

However, after introducing artificial noise, model performance degraded significantly.

### Key Observations

- **Accuracy** decreased from **99.90%** to **14.35%**, indicating that noisy data severely affected overall prediction accuracy.
- **Precision** dropped dramatically from **100%** to approximately **3.71%**, showing that the model produced a large number of false positive predictions.
- **Recall** remained almost unchanged at **97.06%**, indicating that the model continued detecting most machine failure cases despite the noisy inputs.
- **F1-Score** decreased from **0.9851** to **0.0715**, reflecting a substantial decline in balanced classification performance.
- **ROC-AUC** reduced from **0.9901** to **0.8139**, indicating that the model's ability to distinguish between failure and non-failure cases weakened under noisy conditions.

---

## Interpretation

The experimental results suggest that the predictive maintenance model is highly sensitive to corrupted sensor data. Although the model continues to identify most machine failures (high recall), it incorrectly classifies many healthy machines as failures, resulting in extremely low precision and overall accuracy.

This behavior indicates that the model tends to become overly sensitive when input data quality deteriorates.

---

## Conclusion

The noise sensitivity experiment highlights the importance of data quality in predictive maintenance systems. While the trained model performs exceptionally well under clean conditions, its performance deteriorates considerably when exposed to noisy sensor readings.

To improve robustness in real-world Industrial IoT applications, future work may include:

- Applying sensor noise filtering techniques.
- Using feature denoising methods before prediction.
- Training with noise-augmented datasets.
- Exploring more robust machine learning models.
- Implementing anomaly detection before
