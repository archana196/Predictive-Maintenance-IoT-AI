# Week 3: Machine Learning Modeling Preparation

## Project Title

**Manufacturing and Automotive Contextual Predictive Maintenance (IoT Edge AI)**

---

# Overview

Week 3 marks the transition from data preparation and feature engineering to machine learning model development. During Weeks 1 and 2, the team focused on understanding the AI4I 2020 Predictive Maintenance dataset, performing data cleaning, conducting exploratory data analysis, engineering rolling statistical features, and integrating contextual operational information such as ambient temperature, humidity, load density, shift schedules, and day type.

With the contextual dataset now prepared, Week 3 focuses on creating a modeling-ready dataset and establishing a reliable machine learning workflow. The primary goal is to ensure that the dataset is properly structured for predictive modeling while addressing challenges such as class imbalance and validation strategy selection.

Predictive maintenance datasets typically contain significantly fewer machine failure events compared to normal operating records. This imbalance can lead to biased machine learning models that perform well on majority classes but fail to accurately detect actual failures. Therefore, Week 3 introduces techniques that help build more reliable and robust predictive maintenance models.

---

# Week 3 Objective

The objective of Week 3 is to prepare the contextual predictive maintenance dataset for machine learning experimentation and evaluation.

Key objectives include:

* Identifying feature and target variables.
* Preparing a clean modeling dataset.
* Removing non-informative identifier columns.
* Analyzing class distribution and imbalance.
* Researching and implementing Stratified Cross Validation.
* Studying SMOTE for handling class imbalance.
* Understanding LightGBM as a candidate machine learning model.
* Establishing a reproducible modeling workflow for future experiments.

By the end of Week 3, the project should have a well-documented machine learning preparation framework ready for model training and evaluation in subsequent weeks.

---

# Team Responsibilities

The Week 3 activities are distributed among team members to ensure efficient progress and clear ownership of tasks.

| Team Member | Responsibility                                                                           |
| ----------- | ---------------------------------------------------------------------------------------- |
| Archana     | Dataset preparation, target selection, class distribution analysis, project coordination |
| Ajay        | Stratified Cross Validation research and implementation setup                            |
| Abhay       | SMOTE research, implementation planning, and imbalance handling strategy                 |
| Arundhati   | Documentation, README updates, and repository organization                               |

Each member contributes a specific component required for developing a robust machine learning pipeline.

---

# LightGBM Overview

LightGBM (Light Gradient Boosting Machine) is a machine learning framework developed by Microsoft for gradient boosting applications. It is widely used in industrial machine learning projects because of its efficiency, scalability, and predictive performance.

LightGBM builds decision-tree-based models using gradient boosting techniques. Instead of creating a single decision tree, it combines multiple trees to improve prediction accuracy and reduce errors.

### Advantages of LightGBM

* Fast training speed compared to many traditional algorithms.
* Efficient memory usage.
* Excellent performance on structured tabular datasets.
* Ability to handle large datasets with thousands of records.
* Support for complex feature interactions.
* Strong performance on imbalanced classification problems.
* Widely adopted in industrial predictive maintenance systems.

### Relevance to Predictive Maintenance

In predictive maintenance applications, machine failures are influenced by multiple sensor readings and environmental conditions. LightGBM can efficiently learn these relationships and identify patterns associated with future machine failures.

The model is expected to serve as one of the primary algorithms evaluated during the machine learning phase of this project.

---

# Week 3 Deliverables

The following deliverables are planned for Week 3:

## Notebooks

### week3_dataset_preparation.ipynb

Contains:

* Dataset loading
* Feature selection
* Target variable identification
* Removal of unnecessary columns
* Class distribution analysis

### stratified_cv_setup.ipynb

Contains:

* Stratified K-Fold implementation
* Cross-validation workflow examples
* Validation split demonstrations

### smote_research.ipynb

Contains:

* SMOTE experiments
* Oversampling examples
* Data leakage demonstrations
* Integration examples with cross-validation

---

## Documentation Files

### week3_overview.md

Provides:

* Week objectives
* Team responsibilities
* LightGBM overview
* Deliverables summary

### stratified_cv_notes.md

Provides:

* Cross-validation research
* Benefits of stratification
* Workflow explanations

### smote_implementation_plan.md

Provides:

* SMOTE concepts
* Proper implementation methodology
* Data leakage prevention guidelines

---

## Reports

### class_distribution.md

Contains:

* Target class statistics
* Failure percentage calculations
* Class imbalance analysis
* Modeling recommendations

---

# Folder Structure

```text
project/
│
├── notebooks/
│   ├── week3_dataset_preparation.ipynb
│   ├── stratified_cv_setup.ipynb
│   └── smote_research.ipynb
│
├── docs/
│   ├── week3_overview.md
│   ├── stratified_cv_notes.md
│   └── smote_implementation_plan.md
│
├── reports/
│   └── class_distribution.md
│
└── README.md
```

---

# Expected Outcomes

Upon completion of Week 3, the project will have:

* A modeling-ready contextual dataset.
* Clearly defined feature and target variables.
* Comprehensive understanding of class imbalance.
* A validated Stratified Cross Validation workflow.
* A documented SMOTE implementation strategy.
* Foundational knowledge of LightGBM for predictive maintenance.
* Well-organized project documentation for future development.

These outcomes will provide the necessary foundation for Week 4, where machine learning model training, evaluation, and performance comparison activities will begin.

---

# Conclusion

Week 3 serves as a critical bridge between data preparation and machine learning development. By focusing on dataset readiness, validation methodology, imbalance handling, and algorithm research, the team establishes a strong foundation for building reliable predictive maintenance models. The work completed during this phase will directly support accurate machine failure prediction and improve the overall effectiveness of the IoT Edge AI predictive maintenance system.
