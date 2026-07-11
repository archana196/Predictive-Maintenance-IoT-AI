# 🚀 Contextual Predictive Maintenance using IoT and Edge AI

## 📌 Overview

Contextual Predictive Maintenance using IoT and Edge AI is an intelligent machine learning solution designed to predict industrial machine failures before they occur. The system combines IoT sensor data with contextual environmental information to improve prediction accuracy and enable proactive maintenance strategies. By identifying potential failures early, industries can reduce downtime, optimize maintenance schedules, lower operational costs, and improve equipment reliability.

---

## 🎯 Objectives

- Predict machine failures before they occur.
- Minimize unexpected equipment downtime.
- Improve maintenance planning using AI.
- Integrate contextual environmental factors with machine sensor data.
- Build a scalable predictive maintenance pipeline for Industry 4.0 applications.

---

## 📊 Dataset

This project uses the **AI4I 2020 Predictive Maintenance Dataset**, which contains sensor readings collected from industrial machines.

### Features
- Air Temperature
- Process Temperature
- Rotational Speed (RPM)
- Torque
- Tool Wear
- Machine Type
- Failure Labels

Additional contextual features were generated to simulate real-world industrial environments.

---

## 🌍 Contextual Features

To enhance prediction performance, the following contextual information was incorporated:

- Timestamp
- Ambient Temperature
- Humidity
- Load Density
- Work Shift
- Day Type

These features help the model capture environmental and operational conditions affecting machine health.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- LightGBM
- Imbalanced-learn (SMOTE)
- Matplotlib
- Seaborn
- SQLite
- Git & GitHub

---

## ⚙️ Project Workflow

1. Data Collection
2. Data Cleaning & Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Contextual Data Fusion
6. Handling Class Imbalance using SMOTE
7. Model Training using LightGBM
8. Model Evaluation
9. Failure Prediction

---

## 📈 Machine Learning Pipeline

### Data Preprocessing
- Checked missing values
- Removed duplicate records
- Performed exploratory data analysis
- Generated rolling statistical features
- Merged contextual data with sensor data

### Feature Engineering
- Rolling Mean
- Rolling Standard Deviation
- Timestamp Generation
- Ambient Temperature
- Humidity
- Load Density
- Shift
- Day Type

### Handling Class Imbalance
Machine failure cases are relatively rare compared to normal operating conditions. To improve model learning, **SMOTE (Synthetic Minority Oversampling Technique)** was used to balance the dataset.

### Model Training
- Algorithm: **LightGBM Classifier**
- Validation: **Stratified 5-Fold Cross Validation**

---

## 📊 Evaluation Metrics

The model performance was evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC Score
- Confusion Matrix

---

## 📁 Project Structure

```
Predictive-Maintenance-IoT-AI/
│
├── data/
│   ├── ai4i2020.csv
│   ├── timestamps_added.csv
│   ├── external_context.csv
│   ├── context_merged_dataset.csv
│   └── week1_features.csv
│
├── notebooks/
│   ├── Week1_EDA.ipynb
│   ├── Week2_Contextual_Features.ipynb
│   └── Week3_LightGBM_Model.ipynb
│
├── models/
│   └── trained_lightgbm_model.pkl
│
├── results/
│   ├── confusion_matrix.png
│   ├── roc_curve.png
│   └── evaluation_metrics.csv
│
├── README.md
├── requirements.txt
└── LICENSE
```

---

## ✨ Key Features

- Predictive maintenance using machine learning
- IoT sensor data analysis
- Context-aware failure prediction
- Environmental data fusion
- Feature engineering
- Class imbalance handling using SMOTE
- LightGBM-based classification
- Cross-validation for reliable model evaluation
- Industrial AI solution for smart manufacturing

---

## 🚀 Future Enhancements

- Real-time IoT sensor integration
- Edge AI deployment
- Flask-based monitoring dashboard
- MQTT/Kafka streaming support
- Cloud deployment
- Explainable AI using SHAP
- Real-time maintenance alerts
- Deep learning-based predictive models

---

## 🏭 Applications

- Smart Manufacturing
- Industrial IoT (IIoT)
- Automotive Industry
- Energy & Utilities
- Oil & Gas
- Aerospace
- Heavy Machinery
- Predictive Asset Management

---

## 📚 Learning Outcomes

This project strengthened practical knowledge in:

- Machine Learning
- Data Analysis
- Feature Engineering
- Predictive Analytics
- Industrial AI
- IoT Data Processing
- Contextual Data Fusion
- Model Evaluation
- Git & GitHub Collaboration

---

## 👥 Team

**Team Lead**
- Archana V.

**Team Members**
- Ajay
- Abhay
- Arundhati

---

## 📄 License

This project was developed for educational, research, and learning purposes.

---

⭐ If you found this project interesting, feel free to star the repository!
