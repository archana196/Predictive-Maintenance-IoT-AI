Week 3 Documentation Report

Manufacturing and Automotive Contextual Predictive Maintenance (IoT Edge AI)

Introduction

Week 3 focused on the machine learning and model evaluation phase of the Manufacturing and Automotive Contextual Predictive Maintenance project. Following the successful completion of data ingestion, signal processing, contextual data integration, and feature engineering during the first two weeks, the project advanced toward building a predictive maintenance solution capable of identifying potential machine failures before they occur.

The primary objective of this week was to develop and evaluate a machine learning model using the contextual feature dataset prepared in Week 2. Particular emphasis was placed on addressing the class imbalance problem commonly found in predictive maintenance datasets, where machine failure events occur significantly less frequently than normal operating conditions. To overcome this challenge, SMOTE (Synthetic Minority Oversampling Technique) was incorporated into the modeling workflow.

In addition to model development, the team implemented Stratified Cross Validation for reliable performance estimation, compared baseline and balanced models, prepared deployment-ready prediction scripts, initiated Flask dashboard development, and completed comprehensive technical documentation.

---

Week 3 Objectives

The major objectives planned for Week 3 included:

- Develop a baseline LightGBM classification model.
- Evaluate model performance using multiple classification metrics.
- Analyze class imbalance within the machine failure dataset.
- Implement SMOTE to improve minority-class learning.
- Integrate Stratified K-Fold Cross Validation.
- Compare baseline and SMOTE-enhanced models.
- Analyze confusion matrices and minority-class performance.
- Save the final trained model for deployment.
- Create reusable prediction scripts.
- Begin Flask-based dashboard development.
- Prepare project reports, charts, and workflow documentation.

The successful completion of these objectives would establish a strong foundation for deployment activities planned in the following project phase.

---

Dataset Overview

The dataset used for model development was generated through the contextual data fusion process completed during Week 2.

The final dataset combined machine telemetry readings with environmental and operational context features.

Machine Telemetry Features

- Air Temperature
- Process Temperature
- Rotational Speed
- Torque
- Tool Wear

Contextual Features

- Ambient Temperature
- Humidity
- Load Density
- Shift Information
- Day Type

Target Variable

- Machine Failure

By combining machine-level and contextual information, the dataset provided a more realistic representation of industrial operating conditions and enabled the model to learn relationships beyond machine sensor readings alone.

---

Data Preparation and Feature Engineering

Before training the machine learning models, the dataset underwent preprocessing and feature preparation.

Timestamp Processing

The generated timestamp column was converted into useful numerical components, including:

- Hour
- Day
- Weekday
- Month

These derived attributes helped capture temporal behavior patterns that may influence machine performance.

Feature Selection

Relevant predictor variables were selected while excluding unnecessary fields. The resulting feature matrix was prepared for machine learning workflows.

Train-Test Preparation

The dataset was divided into:

- Feature Matrix (X)
- Target Variable (y)

This separation enabled model training and evaluation using standard machine learning techniques.

---

Baseline LightGBM Model Development

Model Selection

LightGBM was chosen as the initial classification algorithm because it offers:

- High efficiency on structured data.
- Fast training speed.
- Strong predictive performance.
- Robust handling of heterogeneous features.
- Feature importance analysis capabilities.

Baseline Training

A baseline model was trained using the original dataset without any balancing techniques.

The purpose of the baseline model was to establish a reference point against which future improvements could be measured.

Evaluation Metrics

The following metrics were selected for performance assessment:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC Score

These metrics provide a balanced understanding of classification performance, particularly for imbalanced datasets.

---

Class Imbalance Analysis

One of the most important challenges encountered during Week 3 was class imbalance.

In predictive maintenance datasets, machine failures occur relatively infrequently compared to normal operating conditions.

Typical Distribution

Normal Samples   ████████████████████████
Failure Samples  ███

Such distributions can lead machine learning models to prioritize the majority class while failing to detect rare but critical failure events.

Impact on Predictive Maintenance

A model may achieve high accuracy while still missing many machine failures.

For industrial applications, failure detection is often more important than overall accuracy because undetected failures may result in:

- Equipment damage
- Production downtime
- Maintenance costs
- Safety risks

Therefore, improving minority-class detection became a key objective.

---

SMOTE Implementation

Purpose

SMOTE (Synthetic Minority Oversampling Technique) was implemented to address class imbalance.

SMOTE creates synthetic examples of minority-class observations, resulting in a more balanced training dataset.

Workflow

To prevent data leakage, SMOTE was applied only within training folds during cross-validation.

Training Fold
      │
      ▼
    SMOTE
      │
      ▼
Model Training
      │
      ▼
Validation Fold Evaluation

This approach ensures that validation data remains completely unseen during training.

Benefits Observed

SMOTE provided several advantages:

- Improved minority-class representation.
- Better learning of failure patterns.
- Increased recall for machine failure predictions.
- More balanced model performance.

---

Stratified Cross Validation

Motivation

Using a single train-test split may produce biased performance estimates, especially for imbalanced datasets.

To improve reliability, Stratified K-Fold Cross Validation was implemented.

Configuration

StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

Procedure

1. Divide the dataset into five folds.
2. Preserve class proportions in every fold.
3. Apply SMOTE to training data only.
4. Train the LightGBM model.
5. Evaluate on the validation fold.
6. Repeat for all folds.
7. Aggregate performance metrics.

Advantages

- Reliable performance estimation.
- Reduced evaluation variance.
- Better utilization of available data.
- Fair comparison between models.

---

Model Performance Evaluation

Performance evaluation was conducted using multiple classification metrics.

Accuracy

Measures overall prediction correctness.

Precision

Measures the proportion of predicted failures that were actually failures.

Recall

Measures the proportion of actual failures that were correctly identified.

F1 Score

Provides a balance between precision and recall.

ROC-AUC

Measures the model's ability to distinguish between normal and failure classes.

These metrics collectively provide a comprehensive evaluation of predictive maintenance performance.

---

Performance Charts

Class Distribution Before and After SMOTE

Before SMOTE

Normal Class   ████████████████████████
Failure Class  ███

After SMOTE

Normal Class   ████████████████████████
Failure Class  ████████████████████████

The balancing process significantly improved minority-class representation during training.

---

Baseline vs SMOTE Comparison

Metric| Baseline Model| SMOTE Model
Accuracy| Improved| Stable
Precision| Moderate| Improved
Recall| Low| Significantly Improved
F1 Score| Moderate| Improved
ROC-AUC| Good| Better

Observations

- Recall increased significantly after SMOTE.
- Failure detection performance improved.
- F1-score increased due to better minority-class learning.
- Overall model robustness improved.

---

Confusion Matrix Analysis

Baseline Model

The baseline model correctly identified most normal operating samples but missed several failure events.

SMOTE Model

The SMOTE-enhanced model improved failure detection and reduced false negatives.

Importance

In predictive maintenance, reducing false negatives is critical because missed failures can lead to unplanned downtime and equipment damage.

The SMOTE-enhanced model demonstrated superior capability in identifying failure events while maintaining acceptable overall performance.

---

Feature Importance Analysis

LightGBM provides feature importance scores that help explain model behavior.

The most influential features included:

1. Tool Wear
2. Torque
3. Rotational Speed
4. Process Temperature
5. Ambient Temperature
6. Load Density

These features showed the strongest contribution toward machine failure prediction.

Feature importance analysis also improves model interpretability and provides useful insights for maintenance engineers.

---

Workflow Diagram

The complete Week 3 workflow is summarized below.

AI4I Dataset
      │
      ▼
Timestamp Generation
      │
      ▼
Context Data Creation
      │
      ▼
Data Fusion
      │
      ▼
Feature Engineering
      │
      ▼
Contextual Dataset
      │
      ▼
Stratified K-Fold CV
      │
      ▼
SMOTE on Training Fold
      │
      ▼
LightGBM Training
      │
      ▼
Model Evaluation
      │
      ▼
Performance Comparison
      │
      ▼
Final Model Selection
      │
      ▼
Save model.pkl
      │
      ▼
Predictor Script
      │
      ▼
Flask Dashboard

---

Deployment Preparation

Several deployment-related components were prepared.

Model Serialization

models/model.pkl

Prediction Utility

src/predictor.py

Batch Prediction Enhancement

src/batch_prediction.py

Flask Application Structure

flask_app/
├── app.py
├── templates/
│   ├── home.html
│   └── dashboard.html
├── static/
└── models/

These components provide the foundation for deploying the predictive maintenance solution as a web application.

---

Week 3 Deliverables

Models

- model.pkl

Scripts

- predictor.py
- batch_prediction.py

Reports

- performance_summary.md
- smote_analysis.md
- cv_results.md
- week3_documentation.md

Documentation

- week3_cv_smote_workflow.md
- README.md

Flask Application

- Home Page
- Dashboard Page
- Bootstrap Layout

---

Conclusion

Week 3 successfully completed the machine learning development phase of the project. A LightGBM-based predictive maintenance model was developed and evaluated using Stratified Cross Validation. Class imbalance challenges were effectively addressed through SMOTE, leading to improved failure detection performance and stronger minority-class metrics.

The team also prepared deployment-ready artifacts, including serialized models, prediction scripts, evaluation reports, workflow documentation, performance visualizations, and an initial Flask application structure. These achievements establish a strong foundation for Week 4 activities, which will focus on application integration, dashboard completion, deployment workflows, and end-to-end predictive maintenance demonstrations.
