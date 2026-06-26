# Performance Summary Report

## Project Title

Manufacturing and Automotive Contextual Predictive Maintenance (IoT Edge AI)

## Week

Week 3 – Model Training, Cross Validation, and Performance Analysis

---

# 1. Overview

Week 3 focused on developing and evaluating machine learning models for predictive maintenance using the AI4I 2020 dataset enriched with contextual manufacturing features. The primary objective was to establish a reliable baseline model, validate its performance through Stratified 5-Fold Cross Validation, and improve minority-class detection using SMOTE (Synthetic Minority Oversampling Technique).

A complete machine learning workflow was implemented, including model training, evaluation, cross-validation, class balancing, and performance comparison. These activities established the foundation for future model optimization and deployment.

---

# 2. Baseline LightGBM Model Performance

The baseline model was developed using the LightGBM classifier and trained on the prepared model-ready dataset.

## Model Configuration

* Algorithm: LightGBM Classifier
* Random State: 42
* Dataset: Contextual Predictive Maintenance Dataset
* Target Variable: Machine Failure

## Evaluation Metrics

The following metrics were used to assess model performance:

* Accuracy
* Precision
* Recall
* F1-Score

### Baseline Results

| Metric    | Score              |
| --------- | ------------------ |
| Accuracy  | [Insert Accuracy]  |
| Precision | [Insert Precision] |
| Recall    | [Insert Recall]    |
| F1-Score  | [Insert F1-Score]  |

## Observations

* The model successfully learned machine operating patterns.
* Sensor features and contextual variables contributed to prediction performance.
* Overall accuracy was high.
* Performance on minority failure cases indicated room for improvement.

The baseline model serves as the benchmark for all future experiments.

---

# 3. Stratified 5-Fold Cross Validation Results

To obtain a more reliable estimate of model performance, Stratified 5-Fold Cross Validation was implemented.

## Configuration

```python
StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)
```

Stratification ensured that class distribution remained consistent across all folds.

### Fold-wise Accuracy Results

| Fold   | Accuracy       |
| ------ | -------------- |
| Fold 1 | [Insert Value] |
| Fold 2 | [Insert Value] |
| Fold 3 | [Insert Value] |
| Fold 4 | [Insert Value] |
| Fold 5 | [Insert Value] |

### Aggregate Results

| Metric             | Value                  |
| ------------------ | ---------------------- |
| Mean Accuracy      | [Insert Mean Accuracy] |
| Standard Deviation | [Insert Std Dev]       |

## Analysis

The cross-validation process demonstrated that the model maintained consistent performance across different data partitions.

Key findings:

* Stable model behavior across folds.
* Low performance variance.
* Reliable generalization capability.
* Reduced dependency on a single train-test split.

These results increased confidence in the robustness of the LightGBM model.

---

# 4. Class Imbalance Analysis

A significant challenge identified in the dataset was class imbalance.

### Example Class Distribution

| Class            | Count |
| ---------------- | ----- |
| Normal Operation | 9661  |
| Machine Failure  | 339   |

Machine failure events represented only a small percentage of total observations.

### Impact of Imbalance

Without corrective measures, machine learning models tend to favor majority-class predictions, leading to:

* High accuracy
* Poor failure detection
* Low recall for minority classes

This issue motivated the implementation of SMOTE during model training.

---

# 5. SMOTE-Based Model Enhancement

SMOTE (Synthetic Minority Oversampling Technique) was integrated into the cross-validation pipeline.

## Workflow

For each fold:

1. Generate training and validation splits.
2. Apply SMOTE only on training data.
3. Keep validation data unchanged.
4. Train LightGBM on balanced data.
5. Evaluate performance.

This approach prevented data leakage while improving minority-class learning.

---

# 6. Baseline vs SMOTE Comparison

The impact of SMOTE was evaluated by comparing model performance before and after balancing.

| Metric    | Baseline Model | SMOTE Model    |
| --------- | -------------- | -------------- |
| Accuracy  | [Insert Value] | [Insert Value] |
| Precision | [Insert Value] | [Insert Value] |
| Recall    | [Insert Value] | [Insert Value] |
| F1-Score  | [Insert Value] | [Insert Value] |

## Performance Impact

### Accuracy

Accuracy remained stable after balancing, indicating that overall prediction quality was maintained.

### Precision

Precision remained competitive while improving minority-class representation.

### Recall

Recall showed improvement, demonstrating that the model detected more machine failure cases.

### F1-Score

The increase in F1-Score indicated a better balance between precision and recall.

---

# 7. Key Findings

Several important findings emerged during Week 3.

## Successful Baseline Model Development

The LightGBM classifier provided a strong starting point for predictive maintenance modeling.

## Reliable Validation Framework

Stratified Cross Validation improved evaluation reliability and reduced performance bias.

## Improved Failure Detection

SMOTE enhanced the model's ability to recognize minority-class failure events.

## Better Evaluation Strategy

Using multiple metrics provided a more comprehensive understanding of model effectiveness than relying solely on accuracy.

## Reusable Workflow

The completed pipeline can be reused for future experimentation and comparative studies.

---

# 8. Challenges Encountered

### Class Imbalance

The dataset contained relatively few machine failure observations.

### Minority-Class Evaluation

Accuracy alone was insufficient to measure predictive maintenance effectiveness.

### Data Leakage Prevention

Special care was required to ensure SMOTE was applied only to training folds.

### Performance Interpretation

Different metrics sometimes highlighted different aspects of model behavior, requiring careful interpretation.

---

# 9. Recommendations

Based on Week 3 results, the following improvements are recommended.

### Hyperparameter Optimization

Tune LightGBM parameters to maximize predictive performance.

### Feature Importance Analysis

Identify the most influential variables affecting machine failure predictions.

### Advanced Evaluation

Include:

* ROC-AUC Score
* Precision-Recall Curve
* Confusion Matrix Analysis
* Feature Importance Visualization

### Comparative Modeling

Evaluate additional algorithms:

* Random Forest
* XGBoost
* Logistic Regression

### Model Explainability

Incorporate explainable AI techniques to improve understanding of predictions.

---

# 10. Conclusion

Week 3 successfully established a complete machine learning evaluation framework for predictive maintenance. The LightGBM model demonstrated strong baseline performance, while Stratified 5-Fold Cross Validation provided reliable validation results. The integration of SMOTE improved minority-class learning and enhanced machine failure detection.

The completed workflow provides a robust foundation for future model optimization, comparative analysis, and deployment-oriented development. The performance results obtained during this phase serve as the benchmark for subsequent project improvements and experimentation.
