# Infotact Banglore Internshi Project 1
# Manufacturing and Automotive Contextual Predictive Maintenance (IoT Edge AI)

## Project Overview

This project focuses on developing a Predictive Maintenance System using the AI4I 2020 Predictive Maintenance Dataset. The goal is to analyze machine operating conditions, identify patterns leading to machine failures, engineer meaningful features, and prepare data for machine learning models capable of predicting equipment failures before they occur.

Predictive maintenance is a key Industry 4.0 application that reduces unexpected downtime, improves operational efficiency, lowers maintenance costs, and increases equipment reliability.

---

# Problem Statement

Manufacturing industries rely heavily on machine availability and operational efficiency. Unexpected machine failures can lead to production delays, financial losses, and maintenance challenges.

The objective of this project is to:

- Analyze machine sensor data.
- Understand machine failure patterns.
- Perform data quality assessment.
- Engineer predictive features.
- Prepare data for machine learning models.
- Support proactive maintenance decisions.

---

# Dataset Description

Dataset Used: AI4I 2020 Predictive Maintenance Dataset

The dataset contains operational parameters collected from industrial machines.

## Dataset Shape

- Rows: 10,000
- Columns: 14

---

# Feature Description

| Feature | Data Type | Description | Unit |
|----------|------------|-------------|------|
| UDI | Integer | Unique Dataset Identifier | - |
| Product ID | Categorical | Product Identification Code | - |
| Type | Categorical | Product Quality Type (L, M, H) | - |
| Air Temperature [K] | Float | Ambient Air Temperature | Kelvin |
| Process Temperature [K] | Float | Process Temperature | Kelvin |
| Rotational Speed [rpm] | Integer | Machine Rotational Speed | RPM |
| Torque [Nm] | Float | Machine Torque | Newton Meter |
| Tool Wear [min] | Integer | Tool Wear Duration | Minutes |
| Machine Failure | Binary | Overall Failure Indicator | 0/1 |
| TWF | Binary | Tool Wear Failure | 0/1 |
| HDF | Binary | Heat Dissipation Failure | 0/1 |
| PWF | Binary | Power Failure | 0/1 |
| OSF | Binary | Overstrain Failure | 0/1 |
| RNF | Binary | Random Failure | 0/1 |

---

# Target Variable

## Machine Failure

| Value | Meaning |
|---------|---------|
| 0 | No Failure |
| 1 | Failure |

The Machine Failure column serves as the primary target variable for predictive modeling.

---

# Week 1: IoT Telemetry Ingestion and Signal Processing



# Project Structure

```text
project/
│
├── data/
│   └── ai4i2020.csv
│
├── docs/
│   ├── dataset_overview.md
│   └── data_dictionary.md
│
├── notebooks/
│   ├── eda.ipynb
│   └── feature_engineering.ipynb
│
├── reports/
│   ├── data_quality_report.md
│   └── week1_summary.md
│
└── README.md
```

---

# File Descriptions

## data/

### [ai4i2020.csv](data/ai4i2020.csv)

Contains the original AI4I 2020 Predictive Maintenance dataset.

Purpose:

- Source dataset for analysis.
- Used in EDA.
- Used in feature engineering.
- Used in model development.

---

## docs/

### [dataset_overview.md](Docs/Dataset overview.md)

Provides a high-level description of the dataset.

Contents:

- Dataset source
- Dataset purpose
- Dataset dimensions
- Feature categories
- Target variable description
- Project relevance

---

### [data_dictionary.md](Docs/data_dictionary.md)

Contains detailed metadata for every feature.

Contents:

- Column names
- Data types
- Descriptions
- Units
- Target variable explanation

Purpose:

Provides documentation that helps team members understand dataset attributes.

---

## notebooks/

### 📄 data_cleaning.ipynb(Notebook/_data_cleaning.ipynb)

Jupyter Notebook containing data preprocessing and cleaning operations performed on the AI4I 2020 Predictive Maintenance Dataset. This notebook includes:
- Missing value analysis
- Duplicate record detection
- Data type validation
- Removal of unnecessary identifier columns (UDI and Product ID)
- Dataset consistency checks
- Preparation of a clean dataset for EDA and feature engineering

### eda.ipynb

Exploratory Data Analysis notebook.

Tasks Performed:

- Dataset loading
- Shape inspection
- Data type verification
- Statistical summary generation
- Missing value analysis
- Duplicate analysis
- Distribution analysis
- Correlation analysis
- Visualization generation

Outputs:

- Histograms
- Boxplots
- Heatmaps
- Failure distribution charts

---

### [feature_engineering_aummery](feature_enginnering_summary.md)

Feature engineering notebook.

Tasks Performed:

- Rolling mean calculation
- Rolling standard deviation calculation
- Trend analysis
- Feature generation

Created Features:

- Air Temperature Rolling Mean
- Process Temperature Rolling Mean
- Rotational Speed Rolling Mean
- Torque Rolling Mean
- Air Temperature Rolling Std
- Process Temperature Rolling Std
- Rotational Speed Rolling Std
- Torque Rolling Std

Purpose:

Generate advanced predictive features for machine learning.

---

## reports/

### [data_quality_report.md](Reports/data_quality_report.md)

Documents dataset quality assessment.

Contents:

- Missing value analysis
- Duplicate detection
- Data type validation
- Data consistency checks
- Summary findings

Key Findings:

- No missing values
- No duplicate records
- Valid data types
- Dataset suitable for modeling

---

### [week1_summary.md](Reports/week1_summary.md)

Summarizes all Week 1 activities.

Contents:

- Dataset understanding
- Data quality assessment
- Exploratory Data Analysis
- Feature engineering progress
- Documentation completed
- Team contributions

Purpose:

Track project progress and internship deliverables.

---

 ### 📄 [week1_report.md](Repots/Week1_report.md)
 
Comprehensive Week 1 project report documenting all activities completed during the first phase of the Predictive Maintenance project. The report includes:
- Project overview and objectives
- Dataset description and statistics
- Data quality assessment
- Exploratory Data Analysis (EDA)
- Failure analysis findings
- Rolling feature engineering activities
- Team contributions and responsibilities
- Key findings and observations
- Deliverables completed during Week 1
- Conclusion and preparation for Week 2 activities
  
# Week 1 Activities Completed

## Dataset Understanding

- Loaded AI4I dataset
- Reviewed dataset structure
- Identified feature categories
- Identified target variable

## Data Quality Assessment

- Checked missing values
- Checked duplicates
- Verified data types
- Validated dataset integrity

## Exploratory Data Analysis

- Generated descriptive statistics
- Examined distributions
- Analyzed machine failures
- Created visualizations

## Feature Engineering

Created rolling statistical features:

### Rolling Mean

- Air Temperature
- Process Temperature
- Rotational Speed
- Torque

### Rolling Standard Deviation

- Air Temperature
- Process Temperature
- Rotational Speed
- Torque

---

# Team Responsibilities

| Team Member | Responsibility |
|-------------|---------------|
| Archana | Dataset loading, EDA, project coordination |
| Ajay | Data cleaning and quality assessment |
| Abhay | Feature engineering and rolling statistics |
| Arundhati | Documentation review and repository management |

---
# week 1: completed 


# Week 2: Contextual Data Integration and Feature Engineering

## Week Objective

The objective of Week 2 was to enrich the AI4I 2020 Predictive Maintenance Dataset by incorporating contextual information that may influence machine behavior and failure patterns. While Week 1 focused on understanding machine telemetry data, Week 2 focused on integrating environmental and operational factors to create a more realistic representation of industrial operating conditions.

The primary goals included:

* Creating a timestamp-enabled machine telemetry dataset.
* Designing and generating a contextual dataset.
* Merging machine and contextual datasets through data fusion.
* Engineering contextual features.
* Performing exploratory analysis on the fused dataset.
* Investigating relationships between contextual variables and machine performance.
* Preparing an enhanced dataset for future machine learning models.

---


### Goals

- Add timestamps to machine sensor records.
- Generate external contextual data.
- Merge contextual data with the AI4I dataset.
- Research contextual feature engineering techniques.
- Analyze relationships between machine and contextual variables.
- Document the data fusion process.
- Prepare the dataset for predictive maintenance modeling.

---


## Timestamp Generation

The original AI4I dataset does not contain timestamps. To support contextual data integration, a timestamp column was generated.

### Process

* Created a continuous timestamp sequence.
* Simulated one machine reading per minute.
* Assigned timestamps to all 10,000 records.
* Verified chronological consistency.

### Outcome

A timestamp-enhanced dataset was created, enabling time-based data fusion and contextual analysis.

---

## Contextual Dataset Design

A synthetic contextual dataset was created to represent environmental and operational conditions within a manufacturing facility.

### Contextual Variables

| Variable            | Description                               |
| ------------------- | ----------------------------------------- |
| Timestamp           | Time reference used for data fusion       |
| Ambient Temperature | Simulated factory environment temperature |
| Humidity            | Simulated atmospheric humidity            |
| Load Density        | Estimated production workload             |
| Shift               | Operational work shift                    |
| Day Type            | Weekday or Weekend                        |

### Purpose

These variables provide additional information that may influence machine stress, operational efficiency, and failure probability.

---

## Data Fusion Process

Data fusion combines machine telemetry information with contextual variables to create a unified analytical dataset.

### Steps Performed

#### 1. Timestamp Validation

Verified timestamp consistency across both datasets.

#### 2. Dataset Alignment

Ensured both datasets shared a common timestamp structure.

#### 3. Merge Operation

Merged datasets using timestamp as the primary key.

#### 4. Data Integrity Verification

Validated:

* Row counts
* Timestamp alignment
* Missing values after merge
* Dataset consistency

### Result

A single fused dataset containing both machine telemetry and contextual information was successfully created.

---

## Contextual Feature Engineering

Additional features were generated to capture relationships between machine operation and contextual conditions.

### Features Created

#### Temperature Difference

Measures thermal variation between machine processes and surrounding environmental conditions.

```text
Temperature Difference =
Process Temperature - Ambient Temperature
```

#### Load Ratio

Represents relative machine workload intensity.

```text
Load Ratio =
Current Load / Maximum Load
```

#### Humidity Impact

Captures environmental influence on machine operation.

#### Shift Encoding

Converts categorical shift information into numerical values for machine learning.

#### Day Type Encoding

Represents weekday and weekend operating conditions.

### Benefits

These engineered features provide meaningful information that cannot be obtained from raw variables alone.

---

## Correlation Analysis

Correlation analysis was performed to investigate relationships among machine telemetry variables and contextual features.

### Objectives

* Identify strong relationships.
* Understand contextual influence on machine behavior.
* Discover potential predictive indicators.

### Findings

#### Temperature Relationships

* Ambient temperature and process temperature exhibit positive correlation.
* Temperature Difference highlights thermal stress conditions.

#### Operational Load Effects

* Load Density influences rotational speed and torque.
* Higher production loads may contribute to machine stress.

#### Environmental Influence

* Humidity shows weak direct relationships but may influence machine behavior indirectly.
* Environmental conditions contribute additional context for failure prediction.

#### Multi-Factor Relationships

Machine failures appear to be influenced by a combination of:

* Temperature
* Torque
* Tool Wear
* Load Density
* Operational Conditions

This supports the use of contextual data for predictive maintenance.

---

## Team Responsibilities

### Archana

* Timestamp generation
* Contextual dataset design
* Dataset integration coordination
* Correlation analysis

### Ajay

* Validation of merged dataset
* Data consistency verification
* Missing value assessment
* Documentation support

### Abhay

* Contextual feature engineering
* Derived feature creation
* Dataset enhancement

### Arundhati

* README updates
* Documentation preparation
* Week 2 report preparation
* Repository organization

---

## Key Findings

1. Timestamp information was successfully added to the AI4I dataset.
2. Contextual environmental and operational datasets were generated.
3. Data fusion was completed successfully.
4. Contextual features provide additional operational insights.
5. Temperature Difference effectively captures machine thermal behavior.
6. Load Density influences operational sensor measurements.
7. Environmental conditions contribute additional predictive information.
8. The fused dataset provides a more realistic representation of industrial environments.
9. Contextual information may improve future machine learning model performance.
10. The project is ready for predictive modeling and ablation studies.

---

## Week 2 Deliverables

Completed deliverables include:

* Timestamp-enhanced AI4I dataset
* Contextual dataset
* Data fusion notebook
* Merged dataset
* Contextual feature engineering notebook
* Correlation analysis report
* Updated README documentation
* Week 2 completion report

---

## Challenges Encountered

* Designing realistic contextual variables.
* Maintaining timestamp consistency during merging.
* Validating data integrity after fusion.
* Ensuring contextual features remained meaningful for predictive maintenance.

These challenges were successfully addressed through validation and testing procedures.

---

## Conclusion

Week 2 objectives were successfully achieved. The AI4I machine telemetry dataset was enhanced with contextual environmental and operational information through a structured data fusion process. Additional contextual features were engineered, and correlation analysis revealed valuable relationships between machine performance and external conditions.

The resulting fused dataset provides a stronger foundation for predictive maintenance modeling than machine telemetry data alone. The project is now prepared to move into Week 3 activities, including machine learning model development, model evaluation, and ablation studies to measure the impact of contextual information on predictive performance.


## Updated Folder Structure

```text
project/
│
├── data/
│   ├── ai4i2020.csv
│   ├── timestamps_added.csv
│   ├── external_context.csv
│   └── merged_context_dataset.csv
│
├── docs/
│   ├── dataset_overview.md
│   ├── data_dictionary.md
│   ├── context_overview.md
│   ├── research_notes.md
│   └── data_fusion_documentation.md
│
├── notebooks/
│   ├── data_cleaning.ipynb
│   ├── eda.ipynb
│   ├── feature_engineering.ipynb
│   ├── correlation_analysis.ipynb
│   └── ablation_study.ipynb
│
├── reports/
│   ├── data_quality_report.md
│   ├── week1_summary.md
│   ├── correlation_report.md
│   └── ablation_study_report.md
│
└── README.md
```

---

## Initial Data Fusion Documentation

### Overview

Data fusion is the process of combining machine sensor data with external contextual information to create a more comprehensive dataset for predictive maintenance analysis.

The AI4I dataset contains machine operational parameters and failure indicators, while the contextual dataset contains environmental and operational conditions that may influence machine performance.

By integrating these datasets, the project can better understand how external factors contribute to machine failures.

---

### Source Datasets

#### AI4I Predictive Maintenance Dataset

Contains machine sensor measurements and failure indicators.

Key variables include:

- Air Temperature [K]
- Process Temperature [K]
- Rotational Speed [rpm]
- Torque [Nm]
- Tool Wear [min]
- Machine Failure

#### External Context Dataset

Contains simulated environmental and operational data.

Variables include:

- Timestamp
- Ambient Temperature
- Load Density
- Humidity
- Shift
- Day Type

---

### Data Fusion Method

The datasets will be merged using the **timestamp** column.

#### Fusion Steps

1. Generate timestamps for all AI4I records.
2. Create external contextual data corresponding to each timestamp.
3. Align both datasets using timestamp values.
4. Merge machine sensor data and contextual data.
5. Validate row counts and data consistency.

---

### Benefits of Data Fusion

- Improves predictive model accuracy.
- Provides environmental context for machine operations.
- Supports advanced feature engineering.
- Enables contextual failure analysis.
- Enhances maintenance planning and decision-making.

---
## Recent Progress

### Contextual Data Integration

External contextual variables were generated and integrated with the AI4I predictive maintenance dataset, including:

* Timestamp
* Ambient Temperature
* Humidity
* Load Density
* Shift
* Day Type

### Feature Engineering

Additional contextual and engineered features were created to enhance predictive maintenance analysis.

Implemented techniques include:

* Shift Encoding
* Day Type Encoding
* Interaction Features
* Lag Features
* Rolling Statistical Features

### Correlation Analysis

Correlation analysis was conducted to examine relationships between contextual variables, engineered features, and machine failure. A correlation heatmap was generated to visualize feature interactions.

### Dataset Validation

The integrated dataset was validated through:

* Missing value checks
* Duplicate detection
* Data type verification
* Feature distribution analysis

### Ablation Study Preparation

An ablation study framework was prepared to compare:

* Internal telemetry features only
* Internal telemetry + contextual features

using Accuracy, Precision, Recall, and F1 Score as evaluation metrics.

### Expected Output

The fusion process will generate a unified dataset containing:

- Machine sensor measurements
- Environmental conditions
- Operational context variables
- Failure indicators

This dataset will be used for feature engineering, correlation analysis, and predictive maintenance model development in subsequent project phases.

# week2 completed

# Week 3: Machine Learning Modeling Preparation

## Objective

The objective of Week 3 is to prepare the contextual predictive maintenance dataset for machine learning model development and evaluation. This phase focuses on creating a modeling-ready dataset, addressing class imbalance issues, researching validation techniques, and establishing a reliable workflow for future machine learning experiments.

Building on the work completed during Weeks 1 and 2, the team will utilize the engineered sensor features and contextual operational data to prepare for predictive maintenance model training.

---

## Key Activities

### Dataset Preparation

* Load the `context_features_dataset.csv` dataset.
* Identify feature columns and target variable.
* Define **Machine Failure** as the prediction target.
* Remove unnecessary identifier columns:

  * UDI
  * Product ID
* Verify dataset integrity before modeling.

### Class Imbalance Analysis

* Analyze the distribution of machine failure and non-failure records.
* Calculate failure percentages.
* Assess the severity of class imbalance.
* Document findings and modeling implications.

### Stratified Cross Validation Research

* Study the concept of Stratified K-Fold Cross Validation.
* Understand why traditional K-Fold may be unsuitable for imbalanced datasets.
* Create sample implementations using Scikit-Learn.
* Establish a validation strategy for future model evaluation.

### SMOTE Research and Planning

* Investigate Synthetic Minority Over-sampling Technique (SMOTE).
* Understand how synthetic samples are generated.
* Identify risks of data leakage.
* Document best practices for applying SMOTE within cross-validation workflows.

### LightGBM Preparation

* Research LightGBM and its applications.
* Study advantages for predictive maintenance tasks.
* Prepare for future model training and performance comparison.

---

## Team Responsibilities

| Team Member | Responsibility                                                                           |
| ----------- | ---------------------------------------------------------------------------------------- |
| Archana     | Dataset preparation, target selection, class distribution analysis, project coordination |
| Ajay        | Stratified Cross Validation research and implementation setup                            |
| Abhay       | SMOTE research and implementation strategy                                               |
| Arundhati   | Documentation, README updates, and repository management                                 |

---

## LightGBM Overview

LightGBM (Light Gradient Boosting Machine) is a gradient boosting framework developed by Microsoft that is designed for efficient and high-performance machine learning.

### Key Advantages

* Fast training speed
* Efficient memory usage
* High predictive accuracy
* Strong performance on structured datasets
* Suitable for large-scale industrial applications
* Effective for predictive maintenance use cases

LightGBM will be evaluated in future weeks as a candidate model for machine failure prediction.

---

## Deliverables

### Notebooks

```text
notebooks/
├── week3_dataset_preparation.ipynb
├── stratified_cv_setup.ipynb
└── smote_research.ipynb
```

### Documentation

```text
docs/
├── week3_overview.md
├── stratified_cv_notes.md
└── smote_implementation_plan.md
```

### Reports

```text
reports/
└── class_distribution.md
```

---

## Folder Structure

```text
project/
│
├── data/
│   ├── ai4i2020.csv
│   ├── timestamps_added.csv
│   ├── context_dataset.csv
│   └── context_features_dataset.csv
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

## Expected Outcomes

By the end of Week 3, the project will achieve:

* A clean and modeling-ready dataset.
* Clearly defined features and target variables.
* Comprehensive class imbalance assessment.
* A documented Stratified Cross Validation workflow.
* A documented SMOTE implementation strategy.
* Initial preparation for machine learning model training.
* Improved project documentation and repository organization.

These outcomes will support Week 4 activities, including machine learning model development, training, validation, and performance evaluation.

---

## Week 3 Completion Status

**Status:** In Progress

### Planned Outputs

* Dataset preparation notebook
* Class distribution report
* Stratified Cross Validation research notes
* SMOTE implementation strategy
* Week 3 documentation updates
* README enhancements

The completion of these deliverables will establish a strong foundation for predictive maintenance model development in the upcoming project phases.



# Technologies Used

## Programming Language

- Python

## Libraries

- Pandas
- NumPy
- Matplotlib
- Seaborn

## Development Environment

- Jupyter Notebook

## Version Control

- Git
- GitHub

---

# Future Work

The following tasks will be completed in upcoming weeks:

## Data Preprocessing

- Feature scaling
- Encoding categorical variables
- Train-test splitting

## Model Development

- Logistic Regression
- Random Forest
- XGBoost
- Gradient Boosting

## Model Evaluation

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

## Deployment

- Model packaging
- API development
- Edge AI integration

---

# Expected Outcomes

- Early failure prediction
- Reduced machine downtime
- Improved maintenance planning
- Increased operational efficiency
- Reliable predictive maintenance solution

---

# Internship Project

Developed as part of the Infotact Solutions Internship Program.

Domain:
Manufacturing and Automotive AI Applications

Project Type:
Predictive Maintenance using Machine Learning and Data Analytics

---

# License

This project is intended for educational, research, and internship learning purposes.
