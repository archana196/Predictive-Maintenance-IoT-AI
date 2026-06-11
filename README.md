# Predictive-Maintenance-IoT-AI

## About the Project
This project predicts machine failures using machine learning techniques on the AI4I Predictive Maintenance Dataset.

## Team Members
- Archana v
- Ajay 
- Abhay soni
- Arundhathi k
  
## Project Architecture Diagram
```text
Dataset
   │
   ▼
Data Collection
   │
   ▼
Data Cleaning & Validation
   │
   ▼
Exploratory Data Analysis (EDA)
   │
   ▼
Feature Engineering
   │
   ▼
Model Development
   │
   ▼
Model Evaluation
   │
   ▼
Predictive Maintenance System
```

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook

## Dataset
AI4I Predictive Maintenance Dataset

## Dataset Statistics
| Metric | Value |
|---------|---------|
| Total Records | 10,000 |
| Total Features | 14 |
| Failure Records | 339 |
| Non-Failure Records | 9,661 |
| Failure Rate | 3.39% |

## Features
- UDI
- Product ID
- Type
- Air Temperature[K]
- Process Temperature[K]
- Rotation Speed[rpm]
- Torque[Nm]
- Tool Wear[min]
- Macxhine Failure
- TWF
- HDF
- PWF
- OSF
- RNF

## Folder Structure

```text
project/
│
├── data/
│   └── ai4i2020.csv
│
├── notebooks/
│   ├── eda.ipynb
│   ├── data_cleaning.ipynb
│   └── feature_engineering.ipynb
│
├── docs/
│   └── data_dictionary.md
│
├── reports/
│   ├── eda_summary.md
│   ├── data_quality_report.md
│   └── feature_engineering_summary.md
│
└── README.md
```

## Week-wise Roadmap

### Week 1 – Data Understanding & Preparation
- Dataset collection
- Data loading
- Exploratory Data Analysis (EDA)
- Data quality assessment
- Feature engineering
- Documentation preparation

### Week 2 – Model Development
- Feature selection
- Model training
- Hyperparameter tuning
- Performance evaluation

### Week 3 – Deployment & Finalization
- Model deployment
- Dashboard creation
- Final documentation
- Project presentation

## Team Responsibilities

| Team Member | Responsibility |
|-------------|----------------|
| Archana | Dataset loading, EDA, project coordination |
| Ajay | Data cleaning and quality assessment |
| Abhay | Feature engineering and rolling statistics |
| Arundhati | Documentation review and repository management |

## How to Run
1. Open Jupyter Notebook
2. Install required libraries
3. Run all notebook cells

## Results
The model predicts potential machine failures and helps improve maintenance planning.
