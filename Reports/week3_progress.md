# Week 3 Progress Report

## Project Title

**Manufacturing and Automotive Contextual Predictive Maintenance (IoT Edge AI)**

### Organization

Infotact Solutions Internship Program

### Week

Week 3 – Machine Learning Model Development and Evaluation

### Duration

Week 3 Project Sprint

---

# 1. Executive Summary

Week 3 marked a significant transition in the project lifecycle, moving from data preparation and feature engineering activities into machine learning model development and evaluation. During this phase, the team focused on building the first predictive maintenance model capable of identifying potential machine failures using sensor data, contextual manufacturing information, and engineered features generated in previous weeks.

The primary machine learning algorithm selected for implementation was LightGBM (Light Gradient Boosting Machine), a high-performance gradient boosting framework known for its speed, efficiency, and effectiveness on structured datasets.

In addition to baseline model training, the team implemented Stratified 5-Fold Cross Validation to ensure reliable performance evaluation and integrated SMOTE (Synthetic Minority Oversampling Technique) to address the class imbalance problem commonly found in predictive maintenance datasets.

The activities completed during Week 3 established a complete machine learning workflow consisting of data preparation, model training, validation, balancing, evaluation, and documentation. The resulting framework serves as the foundation for future model optimization and deployment-oriented development.

---

# 2. Week 3 Objectives

The objectives established for Week 3 were designed to introduce machine learning capabilities into the project while maintaining reproducibility and evaluation reliability.

### Primary Objectives

* Develop an initial LightGBM classification model.
* Create a reproducible machine learning workflow.
* Implement Stratified 5-Fold Cross Validation.
* Handle class imbalance using SMOTE.
* Evaluate model performance using multiple metrics.
* Compare baseline and balanced model performance.
* Document modeling procedures and results.
* Update repository documentation and project tracking systems.

### Expected Outcomes

At the end of Week 3, the team expected to have:

* A trained baseline machine learning model.
* Reliable evaluation procedures.
* Balanced training data workflow.
* Initial performance benchmarks.
* Complete technical documentation.

All planned objectives were successfully completed.

---

# 3. Team Contributions

## 3.1 Archana – LightGBM Model Development and Evaluation

### Responsibilities

Archana was responsible for establishing the project's initial machine learning model.

Tasks included:

* Installing LightGBM and dependencies.
* Loading the model-ready dataset.
* Verifying feature and target structures.
* Creating the model training notebook.
* Training the baseline LightGBM classifier.
* Evaluating prediction performance.
* Coordinating progress across team members.
* Updating GitHub issues and project boards.

### Deliverables

* `notebooks/lightgbm_training.ipynb`
* `notebooks/model_metrics_analysis.ipynb`
* `reports/model_evaluation_report.md`

### Achievements

The baseline LightGBM model was successfully trained and evaluated, providing the first benchmark for predictive maintenance classification within the project.

---

## 3.2 Ajay – Stratified Cross Validation Implementation

### Responsibilities

Ajay focused on creating a reliable model validation framework.

Tasks completed:

* Implemented Stratified 5-Fold Cross Validation.
* Generated training and validation folds.
* Verified class distribution consistency.
* Executed fold-wise evaluation.
* Calculated average model performance.

### Deliverables

* `notebooks/stratified_cv_execution.ipynb`
* `notebooks/stratified_cv_results.ipynb`
* `reports/fold_balance_report.md`
* `reports/cross_validation_results.md`

### Achievements

The cross-validation framework ensured reliable and unbiased performance measurement across multiple data partitions.

---

## 3.3 Abhay – SMOTE Integration and Analysis

### Responsibilities

Abhay was responsible for handling class imbalance issues.

Tasks included:

* Applying SMOTE to training folds.
* Preventing validation data leakage.
* Training LightGBM on balanced datasets.
* Comparing balanced and unbalanced performance.
* Documenting improvements in minority-class detection.

### Deliverables

* `notebooks/smote_cv_pipeline.ipynb`
* `notebooks/smote_lightgbm_analysis.ipynb`
* `reports/smote_results.md`
* `reports/smote_vs_baseline.md`

### Achievements

SMOTE successfully increased minority-class representation and improved the model's ability to identify machine failures.

---

## 3.4 Arundhati – Documentation and Reporting

### Responsibilities

Arundhati managed technical documentation and reporting.

Tasks completed:

* Documenting LightGBM implementation.
* Explaining evaluation metrics.
* Describing cross-validation workflow.
* Documenting SMOTE methodology.
* Creating progress reports.
* Updating project README.

### Deliverables

* `docs/lightgbm_overview.md`
* `docs/model_evaluation_guide.md`
* `reports/performance_summary.md`
* `reports/week3_progress.md`
* `README.md`

### Achievements

Comprehensive documentation was created to support reproducibility, project transparency, and future development.

---

# 4. Technical Activities Completed

## 4.1 LightGBM Model Development

The first machine learning model was implemented using LightGBM.

### Why LightGBM?

LightGBM was selected because it provides:

* Fast training speed.
* Efficient memory usage.
* High predictive performance.
* Support for large feature sets.
* Strong performance on structured data.

### Workflow

1. Dataset loading.
2. Feature-target separation.
3. Data preprocessing.
4. Train-test split.
5. Model initialization.
6. Model training.
7. Prediction generation.
8. Performance evaluation.

This workflow established the project's baseline predictive maintenance model.

---

## 4.2 Stratified 5-Fold Cross Validation

Traditional train-test splits can produce unstable performance estimates.

To address this limitation, Stratified K-Fold Cross Validation was implemented.

### Configuration

* Number of Folds: 5
* Shuffle: Enabled
* Random State: 42

### Benefits

* Preserves class distribution.
* Utilizes the full dataset.
* Produces more reliable results.
* Reduces evaluation variance.

Each fold served as a validation set once while the remaining folds were used for training.

---

## 4.3 Class Imbalance Analysis

One of the major challenges identified was class imbalance.

### Dataset Characteristics

Machine failures represented only a small percentage of observations.

Example:

| Class            | Approximate Count |
| ---------------- | ----------------- |
| Normal Operation | 9661              |
| Failure          | 339               |

This imbalance can cause models to favor majority-class predictions.

---

## 4.4 SMOTE Integration

To address class imbalance, SMOTE was introduced.

### SMOTE Workflow

1. Generate training and validation folds.
2. Apply SMOTE only on training data.
3. Preserve original validation data.
4. Train LightGBM using balanced training data.
5. Evaluate model performance.

### Benefits

* Increased minority-class representation.
* Improved recall.
* Improved F1-score.
* Reduced model bias.

---

# 5. Model Evaluation Activities

The model was evaluated using several classification metrics.

## Accuracy

Measures overall prediction correctness.

## Precision

Measures the quality of positive predictions.

## Recall

Measures the ability to detect actual failures.

## F1-Score

Provides a balanced assessment of precision and recall.

### Additional Analysis

* Fold-wise Accuracy
* Mean Accuracy
* Standard Deviation
* Baseline vs SMOTE Comparison

These metrics provided a complete understanding of model performance.

---

# 6. Key Findings

Several important observations emerged during Week 3.

### Successful Baseline Model

The LightGBM classifier successfully learned patterns from sensor and contextual data.

### Importance of Cross Validation

Cross-validation produced more reliable performance estimates than a single train-test split.

### Impact of SMOTE

SMOTE improved minority-class representation and enhanced machine failure detection.

### Workflow Reusability

The implemented notebooks can be reused for future experiments and model comparisons.

### Improved Project Maturity

The project evolved from data preparation into a fully operational machine learning workflow.

---

# 7. Challenges Encountered

## Class Imbalance

The dataset contained significantly fewer machine failure records.

## Minority-Class Evaluation

Accuracy alone was insufficient to evaluate predictive maintenance effectiveness.

## Data Leakage Risks

Special care was required to ensure SMOTE was applied only to training folds.

## Metric Interpretation

Multiple evaluation metrics were necessary to properly understand model performance.

---

# 8. Deliverables Completed

### Notebooks

* lightgbm_training.ipynb
* model_metrics_analysis.ipynb
* stratified_cv_execution.ipynb
* stratified_cv_results.ipynb
* smote_cv_pipeline.ipynb
* smote_lightgbm_analysis.ipynb

### Documentation

* lightgbm_overview.md
* model_evaluation_guide.md

### Reports

* model_evaluation_report.md
* fold_balance_report.md
* cross_validation_results.md
* smote_results.md
* smote_vs_baseline.md
* performance_summary.md
* week3_progress.md

### Repository Updates

* README.md updated
* GitHub Issues updated
* Project Board synchronized

---

# 9. Lessons Learned

Week 3 provided valuable insights into machine learning development for industrial applications.

Key lessons include:

* High accuracy does not always imply strong failure detection.
* Class balancing is essential for predictive maintenance datasets.
* Cross-validation provides more reliable model evaluation.
* Documentation is critical for reproducibility.
* Feature engineering significantly influences predictive performance.

These lessons will guide future project phases.

---

# 10. Next Steps

The next phase of the project will focus on model improvement and optimization.

Planned activities include:

### Model Optimization

* Hyperparameter tuning
* Feature selection
* Feature importance analysis

### Advanced Evaluation

* ROC-AUC Analysis
* Precision-Recall Curves
* Threshold optimization

### Comparative Modeling

* Random Forest
* XGBoost
* Logistic Regression
* Ensemble Approaches

### Visualization

* Performance dashboards
* Feature importance plots
* Evaluation charts

---

# 11. Conclusion

Week 3 successfully established the machine learning foundation of the Manufacturing and Automotive Contextual Predictive Maintenance project. The team developed a baseline LightGBM classifier, implemented Stratified 5-Fold Cross Validation, integrated SMOTE-based balancing, and created a comprehensive evaluation framework.

The completed workflows provide a robust foundation for future model optimization, experimentation, and deployment activities. Through collaborative effort, the team successfully transitioned from data preparation to predictive modeling, demonstrating the practical application of machine learning techniques in predictive maintenance systems.

The outcomes of Week 3 represent a major milestone in the project and position the team for advanced model development in subsequent phases.
