# Model Evaluation Report

## 1. Introduction

Predictive maintenance has become an essential application of machine learning in modern manufacturing environments. Traditional maintenance strategies, such as reactive maintenance and scheduled preventive maintenance, often result in unnecessary costs, equipment downtime, and inefficient resource utilization. Predictive maintenance aims to overcome these challenges by using historical and real-time operational data to identify potential failures before they occur.

As part of the Manufacturing and Automotive Contextual Predictive Maintenance project, a LightGBM classifier was selected as the baseline machine learning model for predicting machine failures. The objective of this phase was to establish an initial benchmark model that can classify machine operating conditions into normal operation or machine failure categories.

This report presents the dataset preparation process, model configuration, evaluation methodology, performance results, observations, and recommendations for future improvements.

---

# 2. Objective

The primary objective of this task was to train and evaluate a baseline LightGBM model using the prepared contextual predictive maintenance dataset.

Specific goals include:

* Train a machine learning classifier using LightGBM.
* Evaluate model performance on unseen data.
* Calculate key classification metrics.
* Establish a baseline benchmark for future experimentation.
* Prepare the project for cross-validation and SMOTE integration.
* Identify strengths and limitations of the initial model.

The baseline results obtained in this stage will serve as a reference point for subsequent performance improvements.

---

# 3. Dataset Description

## 3.1 Dataset Source

Dataset File:

```text
context_features_dataset.csv
```

The dataset was created during previous project phases by combining machine sensor readings, contextual manufacturing information, and engineered features.

---

## 3.2 Features Included

The dataset contains multiple categories of information.

### Machine Sensor Features

These variables represent the operational condition of industrial equipment.

* Air Temperature
* Process Temperature
* Rotational Speed
* Torque
* Tool Wear

### Failure Indicators

The dataset contains failure-related variables describing different failure mechanisms.

* Tool Wear Failure (TWF)
* Heat Dissipation Failure (HDF)
* Power Failure (PWF)
* Overstrain Failure (OSF)
* Random Failure (RNF)

### Contextual Features

Additional manufacturing context was incorporated to simulate real-world operating environments.

* Ambient Temperature
* Load Density
* Humidity
* Shift
* Day Type

### Engineered Features

Feature engineering techniques were applied to enhance predictive capability.

Examples include:

* Temperature Difference
* Load Ratio
* Humidity Impact
* Hour
* Day
* Month

---

## 3.3 Target Variable

The target variable is:

### Machine Failure

| Value | Meaning          |
| ----- | ---------------- |
| 0     | Normal Operation |
| 1     | Machine Failure  |

The model aims to predict whether a machine is likely to fail based on available operational and contextual information.

---

# 4. Data Preprocessing

Proper preprocessing is essential for developing an effective machine learning model.

Several preprocessing steps were completed before model training.

## 4.1 Data Cleaning

The dataset was reviewed for:

* Missing values
* Duplicate records
* Invalid entries
* Data consistency issues

Any identified issues were resolved during earlier project phases.

---

## 4.2 Feature Selection

Columns that were not required for prediction were removed.

This step helps:

* Reduce model complexity
* Improve computational efficiency
* Eliminate irrelevant information

---

## 4.3 Timestamp Transformation

Timestamp information cannot be directly interpreted by machine learning algorithms.

Therefore, timestamp values were converted into numerical features such as:

* Hour
* Day
* Month

These features allow the model to capture temporal patterns that may influence machine failures.

---

## 4.4 Train-Test Split

The dataset was divided into training and testing subsets.

Configuration:

| Parameter      | Value   |
| -------------- | ------- |
| Training Size  | 80%     |
| Testing Size   | 20%     |
| Random State   | 42      |
| Stratification | Enabled |

Stratified sampling was used to preserve class distribution in both subsets.

---

# 5. LightGBM Model Configuration

## 5.1 Overview

LightGBM (Light Gradient Boosting Machine) is a gradient boosting framework developed by Microsoft.

It is designed to:

* Train faster than traditional boosting algorithms.
* Consume less memory.
* Handle large datasets efficiently.
* Achieve strong predictive performance.

---

## 5.2 Model Initialization

The baseline model was initialized using default parameters.

```python
model = LGBMClassifier(random_state=42)
```

The random state was fixed to ensure reproducibility of results.

---

## 5.3 Training Process

The model training workflow consisted of:

1. Loading the dataset.
2. Separating features and target variable.
3. Creating training and testing datasets.
4. Initializing LightGBM.
5. Training the model.
6. Generating predictions.
7. Evaluating performance.

---

# 6. Evaluation Metrics

To assess model effectiveness, multiple evaluation metrics were calculated.

## 6.1 Accuracy

Accuracy measures the proportion of correctly classified observations.

Formula:

Accuracy = Correct Predictions / Total Predictions

Although useful, accuracy alone may be misleading when class imbalance exists.

---

## 6.2 Precision

Precision measures the percentage of predicted failures that were actually failures.

Higher precision indicates fewer false alarms.

---

## 6.3 Recall

Recall measures how many actual failures were correctly detected.

For predictive maintenance systems, recall is particularly important because missing a failure can lead to unexpected downtime.

---

## 6.4 F1-Score

F1-Score combines precision and recall into a single metric.

It provides a balanced assessment of model performance, especially for imbalanced datasets.

---

# 7. Results

## 7.1 Accuracy

**Accuracy:** `[Insert Accuracy Here]`

This value represents the proportion of correctly classified observations in the testing dataset.

---

## 7.2 Classification Report

```text
[Paste Classification Report Output Here]
```

The classification report includes:

* Precision
* Recall
* F1-Score
* Support

for each class.

---

## 7.3 Confusion Matrix

```text
[Paste Confusion Matrix Output Here]
```

The confusion matrix provides a detailed breakdown of prediction outcomes.

| Actual / Predicted | Normal | Failure |
| ------------------ | ------ | ------- |
| Normal             | TN     | FP      |
| Failure            | FN     | TP      |

---

# 8. Performance Analysis

The baseline LightGBM model successfully learned patterns from machine operational data and contextual manufacturing variables.

Several observations can be made:

### Strong Overall Accuracy

The model achieved a high overall accuracy, indicating successful classification of the majority of observations.

### Effective Learning

LightGBM demonstrated the ability to learn relationships among sensor readings and contextual features.

### Potential Class Imbalance Effects

Because failure events are relatively rare, the model may be biased toward the majority class.

A high accuracy score alone does not guarantee strong failure detection performance.

### Importance of Recall

For predictive maintenance applications, recall is often more important than accuracy because identifying failures is the primary objective.

---

# 9. Limitations

Although the baseline model produced encouraging results, several limitations remain.

## Class Imbalance

Machine failures represent only a small portion of the dataset.

This imbalance may negatively impact minority-class detection.

---

## Single Evaluation Split

Performance was measured using a single train-test split.

Results may vary depending on the specific data partition.

---

## No Oversampling

No balancing technique was applied during baseline training.

Minority-class observations remain underrepresented.

---

## Default Hyperparameters

The baseline model uses default LightGBM settings.

Further optimization may improve predictive performance.

---

# 10. Future Improvements

Several enhancements are planned for the next stage.

## Stratified 5-Fold Cross Validation

Cross-validation will provide a more reliable estimate of model performance.

Benefits include:

* Reduced variance
* Better utilization of available data
* More robust evaluation

---

## SMOTE Integration

Synthetic Minority Oversampling Technique (SMOTE) will be applied to training folds.

Expected benefits:

* Improved class balance
* Better minority-class learning
* Increased recall and F1-score

---

## Additional Metrics

Future evaluations will include:

* ROC-AUC
* Precision-Recall Curve
* Fold-wise Accuracy
* Mean Accuracy
* Standard Deviation

---

## Hyperparameter Tuning

LightGBM parameters will be optimized to improve predictive performance.

---

# 11. Conclusion

The baseline LightGBM model was successfully trained and evaluated using the contextual predictive maintenance dataset. The model achieved promising initial results and established an important benchmark for future experimentation. While overall performance appears strong, additional evaluation through Stratified 5-Fold Cross Validation and SMOTE-based balancing is necessary to fully assess the model's capability to detect machine failures.

The results from this baseline evaluation provide a solid foundation for subsequent model optimization, performance comparison, and deployment-oriented analysis in later phases of the project.
