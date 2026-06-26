# LightGBM Overview

## 1. Introduction

Predictive maintenance is one of the most important applications of machine learning in modern manufacturing environments. Instead of performing maintenance at fixed intervals or waiting for equipment failures to occur, predictive maintenance uses historical and real-time data to forecast machine failures before they happen.

In this project, the AI4I 2020 Predictive Maintenance dataset is combined with contextual manufacturing information and engineered features to build a machine failure prediction system. To develop the first machine learning model, LightGBM (Light Gradient Boosting Machine) has been selected as the baseline classification algorithm.

LightGBM is a gradient boosting framework developed by Microsoft that is designed for efficiency, scalability, and high predictive performance. It is widely used in industrial machine learning applications because it can process large datasets quickly while maintaining strong accuracy.

The goal of Week 3 is to establish a reliable modeling pipeline using LightGBM, Stratified Cross Validation, and SMOTE-based class balancing techniques.

---

## 2. What is LightGBM?

LightGBM (Light Gradient Boosting Machine) is an open-source machine learning framework based on Gradient Boosting Decision Trees (GBDT).

Gradient Boosting works by building multiple decision trees sequentially. Each new tree attempts to correct the errors made by the previous trees. By combining many weak learners, the algorithm produces a strong predictive model capable of handling complex relationships within data.

LightGBM improves traditional gradient boosting methods by introducing several optimizations:

* Histogram-based learning
* Leaf-wise tree growth
* Faster training speed
* Lower memory consumption
* Efficient handling of large datasets

These characteristics make LightGBM particularly suitable for predictive maintenance tasks where numerous sensor measurements and contextual variables interact to influence machine behavior.

---

## 3. Why LightGBM Was Selected

Several machine learning algorithms can be used for classification problems, including Logistic Regression, Decision Trees, Random Forests, Support Vector Machines, and XGBoost.

LightGBM was selected for the following reasons:

### 3.1 High Performance

LightGBM consistently achieves high predictive accuracy on structured datasets. Since the AI4I dataset consists primarily of tabular sensor data, LightGBM is expected to perform effectively.

### 3.2 Fast Training

Industrial datasets may contain thousands or millions of observations. LightGBM's optimized architecture enables faster model training compared to many traditional algorithms.

### 3.3 Scalability

As additional contextual datasets are integrated into the project, the number of features may continue to increase. LightGBM can efficiently handle larger feature spaces without significant performance degradation.

### 3.4 Feature Importance Analysis

Understanding the factors contributing to machine failures is important in predictive maintenance. LightGBM provides feature importance scores that help identify which variables have the greatest impact on predictions.

### 3.5 Compatibility with Cross Validation

LightGBM integrates seamlessly with Stratified K-Fold Cross Validation, making it suitable for robust model evaluation.

---

## 4. Dataset Used for Training

The model is trained using the Week 2 model-ready dataset, which combines machine telemetry data with external contextual information and engineered features.

### 4.1 Original Sensor Features

The AI4I dataset provides operational measurements collected from industrial machines.

| Feature             | Description                     |
| ------------------- | ------------------------------- |
| Air Temperature     | Ambient machine temperature     |
| Process Temperature | Internal process temperature    |
| Rotational Speed    | Machine rotational speed in RPM |
| Torque              | Applied torque                  |
| Tool Wear           | Tool wear duration              |

### 4.2 Failure Indicators

The dataset includes failure-specific indicators that describe different failure mechanisms.

| Feature | Description              |
| ------- | ------------------------ |
| TWF     | Tool Wear Failure        |
| HDF     | Heat Dissipation Failure |
| PWF     | Power Failure            |
| OSF     | Overstrain Failure       |
| RNF     | Random Failure           |

### 4.3 Contextual Manufacturing Features

Additional environmental and operational context was created during Week 2.

| Feature             | Description                        |
| ------------------- | ---------------------------------- |
| Ambient Temperature | External environmental temperature |
| Load Density        | Machine workload intensity         |
| Humidity            | Environmental humidity             |
| Shift               | Production shift                   |
| Day Type            | Weekday or weekend indicator       |

### 4.4 Engineered Features

New variables were created to improve predictive capability.

| Feature         | Description                                    |
| --------------- | ---------------------------------------------- |
| Temp Difference | Difference between process and air temperature |
| Load Ratio      | Relative workload measure                      |
| Humidity Impact | Combined humidity influence metric             |
| Hour            | Hour extracted from timestamp                  |
| Day             | Day extracted from timestamp                   |
| Month           | Month extracted from timestamp                 |

---

## 5. Target Variable

The target variable used for model training is:

### Machine Failure

| Value | Meaning          |
| ----- | ---------------- |
| 0     | Normal Operation |
| 1     | Machine Failure  |

The objective of the model is to predict whether a machine will fail based on current operating conditions and contextual information.

This is a binary classification problem.

---

## 6. Class Imbalance Challenge

One of the major challenges in predictive maintenance datasets is class imbalance.

In the AI4I dataset, normal machine operations significantly outnumber machine failure events.

Example distribution:

| Class            | Count |
| ---------------- | ----- |
| Normal Operation | 9661  |
| Machine Failure  | 339   |

This means that approximately 96.6% of observations belong to the majority class.

If class imbalance is not addressed, the model may become biased toward predicting normal operations and fail to identify actual machine failures.

To overcome this issue:

* Stratified Cross Validation preserves class distribution.
* SMOTE is applied to training folds.
* Validation data remains untouched.
* Model evaluation focuses on balanced assessment across classes.

---

## 7. Training Workflow

The Week 3 modeling workflow follows a structured machine learning pipeline.

### Step 1: Load Dataset

The model-ready dataset is loaded into a Pandas DataFrame.

### Step 2: Feature and Target Separation

The dataset is divided into:

* X → Input Features
* y → Machine Failure Target

### Step 3: Data Preparation

Timestamp information is converted into numerical time-based features.

### Step 4: Stratified 5-Fold Cross Validation

The dataset is split into five folds while maintaining class distribution.

### Step 5: Apply SMOTE

Synthetic Minority Oversampling Technique (SMOTE) is applied only to training data.

### Step 6: Train LightGBM

The LightGBM classifier is trained on balanced training data.

### Step 7: Model Evaluation

Performance metrics are calculated on validation data for each fold.

### Step 8: Performance Aggregation

Results from all folds are combined to obtain overall model performance.

---

## 8. Expected Benefits

The implementation of LightGBM is expected to provide several advantages:

### Improved Failure Detection

The model should identify potential machine failures before breakdowns occur.

### Reduced Downtime

Early detection allows maintenance teams to intervene proactively.

### Better Resource Planning

Maintenance schedules can be optimized based on predicted failure risks.

### Increased Operational Efficiency

Reducing unexpected failures improves production continuity and equipment utilization.

### Data-Driven Decision Making

Model predictions support informed maintenance strategies rather than reactive approaches.

---

## 9. Week 3 Deliverables

The LightGBM implementation contributes to the following Week 3 deliverables:

* `notebooks/lightgbm_training.ipynb`
* `notebooks/stratified_cv_execution.ipynb`
* `notebooks/smote_cv_pipeline.ipynb`
* `reports/fold_balance_report.md`
* `reports/smote_results.md`
* `docs/lightgbm_overview.md`
* `reports/week3_progress.md`

---

## 10. Conclusion

LightGBM serves as the baseline machine learning model for the Manufacturing and Automotive Contextual Predictive Maintenance project. Its ability to efficiently process structured industrial data, handle complex feature interactions, and support scalable model development makes it an appropriate choice for machine failure prediction.

Through the integration of contextual manufacturing variables, engineered features, Stratified 5-Fold Cross Validation, and SMOTE-based balancing, the Week 3 modeling pipeline establishes a strong foundation for predictive maintenance analytics. The results obtained from this baseline model will guide future optimization, evaluation, and comparison activities in subsequent project phases.
