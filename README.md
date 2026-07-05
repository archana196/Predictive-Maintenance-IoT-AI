# Predictive Maintenance System using IoT, Context-Aware AI, and LightGBM

## Overview

The **Predictive Maintenance System** is an intelligent machine failure prediction application that combines industrial sensor data, contextual environmental features, and machine learning to predict equipment failures before they occur.

The project is developed using the **AI4I Predictive Maintenance Dataset** and enhanced with additional contextual parameters such as ambient temperature, humidity, operational shift, and day type. A **LightGBM** classifier is trained to classify whether a machine is likely to fail, and a **Flask web application** provides an interactive interface for real-time predictions.

---

## Objectives

* Predict machine failures before they occur.
* Reduce unexpected machine downtime.
* Support preventive maintenance decisions.
* Improve industrial reliability through AI-powered predictions.
* Provide an easy-to-use web interface for maintenance engineers.

---

## Features

* Context-aware machine failure prediction
* LightGBM machine learning model
* Flask-based web application
* Real-time prediction with confidence score
* User-friendly Bootstrap interface
* Feature engineering using environmental and operational data
* Model trained using only the most important features
* Professional project structure suitable for deployment

---

## Technologies Used

### Programming Language

* Python 3.x

### Machine Learning

* LightGBM
* Scikit-learn
* Pandas
* NumPy

### Web Framework

* Flask

### Frontend

* HTML5
* Bootstrap 5
* CSS

### Model Serialization

* Joblib

---

## Dataset

Dataset used:

**AI4I 2020 Predictive Maintenance Dataset**

Additional contextual features were engineered to improve prediction performance.

---

## Context Features Added

The project extends the original dataset by introducing additional contextual information.

* Ambient Temperature
* Load Density
* Humidity
* Shift
* Day Type

These features help improve the robustness of machine failure prediction.

---

## Final Model Features

The final LightGBM model is trained using the following **11 essential features**:

1. Type
2. Air Temperature (K)
3. Process Temperature (K)
4. Rotational Speed (RPM)
5. Torque (Nm)
6. Tool Wear (min)
7. Ambient Temperature
8. Load Density
9. Humidity
10. Shift
11. Day Type

---

## Project Workflow

1. Load industrial sensor dataset
2. Perform preprocessing
3. Engineer contextual features
4. Encode categorical variables
5. Train LightGBM classifier
6. Evaluate model performance
7. Save trained model
8. Integrate model with Flask
9. Predict machine condition using user inputs
10. Display prediction probability and machine health status

---

## Project Structure

```text
Predictive-Maintenance-IoT-AI
│
├── app.py
├── README.md
├── requirements.txt
│
├── data
│   ├── ai4i2020.csv
│   ├── context_merged_dataset.csv
│   ├── model_ready_dataset.csv
│
├── models
│   ├── model.pkl
│   └── encoders.pkl
│
├── notebooks
│   ├── week3_modeling_setup.ipynb
│   ├── contextual_feature_engineering.ipynb
│   ├── correlation_analysis.ipynb
│
├── reports
│
├── static
│   ├── css
│   ├── images
│
├── templates
│   ├── index.html
│   └── result.html
│
├── utils
│   └── predictor.py
│
└── test_predictor.py
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/your-username/Predictive-Maintenance-IoT-AI.git
```

Move into the project

```bash
cd Predictive-Maintenance-IoT-AI
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## Machine Learning Model

Algorithm:

* LightGBM Classifier

Reasons for selection:

* High prediction accuracy
* Fast training speed
* Efficient handling of tabular data
* Excellent performance on industrial datasets
* Feature importance analysis support

---

## Input Parameters

The web application accepts the following inputs:

* Machine Type
* Air Temperature
* Process Temperature
* Rotational Speed
* Torque
* Tool Wear
* Ambient Temperature
* Load Density
* Humidity
* Shift
* Day Type

---

## Output

The application predicts:

* Machine Health Status
* Failure Probability
* Healthy or Failure Classification

---

## Future Enhancements

* IoT sensor integration
* MQTT real-time data streaming
* Cloud deployment
* Predictive maintenance dashboard
* Email and SMS alerts
* Maintenance scheduling system
* Historical prediction logs
* Interactive analytics dashboard

---

## Acknowledgements

* AI4I 2020 Predictive Maintenance Dataset
* LightGBM
* Scikit-learn
* Flask
* Bootstrap

---

## License

This project is developed for educational and internship purposes.


