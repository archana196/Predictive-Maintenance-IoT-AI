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

The objective of Week 2 is to enhance the predictive maintenance system by integrating external contextual information with machine sensor data. This phase focuses on generating contextual variables, performing data fusion, researching advanced feature engineering techniques, and preparing the dataset for improved predictive maintenance analysis.

### Goals

- Add timestamps to machine sensor records.
- Generate external contextual data.
- Merge contextual data with the AI4I dataset.
- Research contextual feature engineering techniques.
- Analyze relationships between machine and contextual variables.
- Document the data fusion process.
- Prepare the dataset for predictive maintenance modeling.

---

## Team Responsibilities

| Team Member | Responsibilities |
|------------|------------------|
| Archana | Add timestamps to AI4I dataset, merge contextual data, perform correlation analysis, conduct ablation study, manage GitHub issues and project board |
| Ajay | Generate external contextual dataset including ambient temperature, load density, humidity, shift, and day type |
| Abhay | Research contextual feature engineering methods, identify new features, prepare implementation notebook and research notes |
| Arundhati | Create contextual variable documentation, update README, prepare data fusion documentation |

---

## Deliverables

### Archana
- `timestamps_added.csv`
- `merged_context_dataset.csv`
- `correlation_analysis.ipynb`
- `ablation_study.ipynb`

### Ajay
- `external_context.csv`

### Abhay
- `feature_engineering.ipynb`
- `research_notes.md`

### Arundhati
- `context_overview.md`
- `data_fusion_documentation.md`
- Updated `README.md`

---

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
