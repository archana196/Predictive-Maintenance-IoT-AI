# Infotact Bangalore Internship – Project 1

# Manufacturing & Automotive Contextual Predictive Maintenance (IoT Edge AI)

## Internship Details

| Field                   | Details                                                                    |
| ----------------------- | -------------------------------------------------------------------------- |
| Internship Organization | Infotact Bangalore                                                         |
| Internship Domain       | Artificial Intelligence & Machine Learning                                 |
| Project Title           | Manufacturing & Automotive Contextual Predictive Maintenance (IoT Edge AI) |
| Project Duration        | Internship Project – Phase 1                                               |
| Team Type               | Collaborative Team Project                                                 |
| Technology Stack        | Python, Flask, LightGBM, Pandas, NumPy, Scikit-Learn, Bootstrap 5, SQLite |
| Dataset                 | AI4I 2020 Predictive Maintenance Dataset                                   |

---

## Team Members

| Name        |
| ----------- |
| Ajay Verma  |
| Archana     |
| Abhay       |
| Arundhati   |

---

## Project Abstract

Predictive maintenance is a critical application of Artificial Intelligence in modern manufacturing and automotive industries. Unexpected equipment failures can lead to significant downtime, increased maintenance costs, production losses, and safety risks.

This project develops an AI-powered Predictive Maintenance System capable of identifying potential machine failures before they occur by analyzing machine telemetry data and contextual environmental information.

The system combines Industrial IoT sensor measurements with contextual variables such as ambient temperature, load density, humidity, work shifts, and day type to create a more realistic industrial environment for predictive modeling.

A full-stack Flask web application was built and deployed, allowing authenticated users to run real-time predictions using a trained LightGBM model, view personalized prediction history, and download their own prediction records.

---

## Problem Statement

Traditional maintenance approaches are generally classified into:

### Reactive Maintenance
* Maintenance is performed only after failure occurs.
* Results in costly downtime.
* Increases operational risk.

### Preventive Maintenance
* Maintenance is performed on a fixed schedule.
* May replace components unnecessarily.
* Increases maintenance cost.

### Predictive Maintenance
* Maintenance decisions are based on actual machine condition.
* Failures can be predicted before occurrence.
* Improves operational efficiency and equipment reliability.

This project implements Predictive Maintenance using Artificial Intelligence and Industrial IoT data, delivered through a secure, authenticated web dashboard.

---

## Project Objectives

* Analyze machine telemetry data.
* Perform data cleaning and validation.
* Generate contextual environmental datasets.
* Integrate telemetry and contextual information.
* Engineer meaningful predictive features.
* Perform exploratory and correlation analysis.
* Develop machine learning models for failure prediction.
* Evaluate model performance using Stratified Cross Validation.
* Deploy the model through a secure, production-quality Flask web application.
* Support proactive maintenance decision-making.

---

## Business Impact

The proposed solution helps industries:

* Reduce unexpected equipment failures.
* Minimize machine downtime.
* Improve maintenance planning.
* Increase equipment lifespan.
* Optimize production efficiency.
* Reduce operational and maintenance costs.
* Enable data-driven maintenance decisions.

---

## Technology Stack

### Machine Learning
| Library         | Purpose                              |
|-----------------|--------------------------------------|
| LightGBM        | Primary prediction model             |
| Scikit-Learn    | Preprocessing, CV, evaluation        |
| imbalanced-learn| SMOTE oversampling                   |
| Pandas          | Data manipulation                    |
| NumPy           | Numerical computing                  |
| Matplotlib      | Visualization                        |
| Joblib          | Model serialization                  |

### Web Application
| Technology      | Purpose                              |
|-----------------|--------------------------------------|
| Flask 3.x       | Web framework                        |
| SQLite          | User authentication database         |
| Werkzeug        | Password hashing (bcrypt)            |
| Bootstrap 5.3   | Responsive UI framework              |
| Bootstrap Icons | Icon library                         |
| Google Fonts    | Inter typography                     |

### Development Tools
| Tool            | Purpose                              |
|-----------------|--------------------------------------|
| Jupyter Notebook| Model development & EDA              |
| Git / GitHub    | Version control                      |
| Python 3.x      | Primary language                     |

### Dataset Source
AI4I 2020 Predictive Maintenance Dataset — UCI Machine Learning Repository

---

## Project Structure

```text
Predictive-Maintenance-IoT-AI/
│
├── data/
│   ├── ai4i2020.csv                   ← Original dataset
│   ├── preprocessed_ai4i2020.csv      ← Cleaned dataset
│   ├── timestamps_added.csv           ← Timestamp-enhanced dataset
│   ├── external_context.csv           ← Synthetic contextual data
│   ├── contextual_merged_dataset.csv  ← Merged telemetry + context
│   └── prediction_history.csv         ← Live prediction log (all users)
│
├── notebook/                          ← Jupyter notebooks (EDA, modeling)
├── docs/                              ← Project documentation
├── reports/                           ← Analysis reports
│
├── flask_app/
│   ├── app.py                         ← Main Flask application
│   ├── requirements.txt               ← Python dependencies
│   │
│   ├── model/
│   │   ├── model.pkl                  ← Trained LightGBM model
│   │   └── encoders.pkl               ← Label encoders (Type, Shift, Day_Type)
│   │
│   ├── database/
│   │   └── users.db                   ← SQLite user accounts database
│   │
│   ├── static/
│   │   └── css/
│   │       └── style.css              ← Dark glassmorphism theme
│   │
│   ├── templates/
│   │   ├── base.html                  ← Base layout (navbar, footer, flash)
│   │   ├── login.html                 ← User login page
│   │   ├── signup.html                ← User registration page
│   │   ├── index.html                 ← Prediction dashboard
│   │   ├── results.html               ← Prediction result page
│   │   └── history.html               ← Personalized prediction history
│   │
│   └── utils/
│       └── history_logger.py          ← CSV prediction logging utility
│
└── README.md
```

---

## How to Run

### Prerequisites

Ensure the following are installed:

```bash
Python 3.8+
pip
```

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/archana196/Predictive-Maintenance-IoT-AI.git
cd Predictive-Maintenance-IoT-AI

# 2. Install dependencies
pip install -r flask_app/requirements.txt

# 3. Start the Flask application
cd flask_app
python app.py
```

### Access the Application

Open your browser and navigate to:

```
http://127.0.0.1:5000
```

---

## Application Flow

```text
/signup  →  Create an account
    ↓
/login   →  Authenticate with email & password
    ↓
/        →  Machine Health Dashboard (prediction form)
    ↓
/predict →  Submit 11 IoT features → LightGBM prediction
    ↓
/results →  View result: Healthy / Failure, Confidence %, Risk Level
    ↓
/history →  View YOUR last 5 predictions (personalized)
    ↓
/download_history → Download YOUR prediction records as CSV
    ↓
/logout  →  Clear session, redirect to login
```

---

## LightGBM Model — Input Features

The trained LightGBM model accepts exactly **11 features**:

| # | Feature               | Type        | Description                          |
|---|-----------------------|-------------|--------------------------------------|
| 1 | Type                  | Categorical | Machine quality type: L / M / H      |
| 2 | Air_temperature_K     | Numeric     | Air temperature in Kelvin            |
| 3 | Process_temperature_K | Numeric     | Process temperature in Kelvin        |
| 4 | Rotational_speed_rpm  | Numeric     | Rotational speed in RPM              |
| 5 | Torque_Nm             | Numeric     | Torque in Newton-meters              |
| 6 | Tool_wear_min         | Numeric     | Tool wear time in minutes            |
| 7 | Ambient_Temperature   | Numeric     | Ambient temperature in °C            |
| 8 | Load_Density          | Numeric     | Load density percentage (0–100)      |
| 9 | Humidity              | Numeric     | Humidity percentage (0–100)          |
| 10| Shift                 | Categorical | Work shift: Morning / Evening / Night|
| 11| Day_Type              | Categorical | Day type: Weekday / Weekend          |

**Categorical Encoding:** `Type`, `Shift`, and `Day_Type` are encoded using `encoders.pkl` (LabelEncoder) before prediction.

**Model Output:**
- `0` → Healthy
- `1` → Failure

---

## Flask Web Application — Features

### Authentication (Part 1)
- User Signup with name, email, password
- Password hashing using `werkzeug.security` (bcrypt — never stored in plain text)
- User Login with session management
- Logout — clears session
- `login_required` decorator protects all dashboard routes
- Duplicate email detection with user-friendly flash message
- Invalid login handling

### Prediction Dashboard (Part 2)
- Dark glassmorphism premium UI (Bootstrap 5.3 + custom CSS)
- Animated hero section with rotating background
- 4 stat cards: AI Model · 11 Features · Real-time · Secure
- Form divided into 4 sections:
  - Machine Configuration (Type, Shift, Day Type)
  - Temperature Readings (Air, Process, Ambient)
  - Mechanical Parameters (RPM, Torque, Tool Wear)
  - Environmental Conditions (Load Density, Humidity)
- Loading spinner on form submission

### Prediction Results (Part 3)
- Pulsing green border for Healthy / red border for Failure
- Bouncing status icon animation
- Animated confidence progress bar
- Risk Level badge: 🟢 Low / 🟡 Medium / 🔴 High
- Prediction timestamp
- Three action buttons: Predict Again · View History · Logout

**Risk Level Logic:**
```
Healthy prediction          → Low   (always)
Failure + confidence < 70%  → Medium
Failure + confidence ≥ 70%  → High
```

### Personalized History (Part 4)
- Each user sees ONLY their own predictions (filtered by email)
- Shows last 5 predictions, most recent first
- Live client-side search (JavaScript) across all columns
- Mini inline confidence progress bars per row
- Colored risk badges in table
- Total prediction count for the logged-in user

### Personalized CSV Download (Part 5)
- Downloads ONLY the current user's prediction records
- Filtered in-memory — shared CSV on disk is never modified
- Download filename: `history_<email>.csv`
- Flash message if no predictions exist yet

---

## Data Architecture

### users.db (SQLite)

```
users table:
┌────┬──────────┬─────────────────┬──────────────────────────────┐
│ id │ name     │ email           │ password                     │
├────┼──────────┼─────────────────┼──────────────────────────────┤
│ 1  │ Ajay     │ ajay@gmail.com  │ pbkdf2:sha256:XXXX... (hash) │
│ 2  │ Archana  │ archana@...     │ pbkdf2:sha256:YYYY... (hash) │
└────┴──────────┴─────────────────┴──────────────────────────────┘
```

### prediction_history.csv (Shared Log)

```
Columns:
Timestamp | Machine Type | Prediction | Probability | Risk Level | User Email
```

All users write to the same CSV. The `User Email` column is used to filter records per user at read time.

---

## Dataset Information

| Property       | Value                                 |
|----------------|---------------------------------------|
| Dataset        | AI4I 2020 Predictive Maintenance      |
| Source         | UCI Machine Learning Repository       |
| Total Records  | 10,000                                |
| Total Features | 14 original + 5 contextual = 19       |
| Target         | Machine Failure (binary: 0 / 1)       |

### Failure Categories
| Code | Name                      |
|------|---------------------------|
| TWF  | Tool Wear Failure         |
| HDF  | Heat Dissipation Failure  |
| PWF  | Power Failure             |
| OSF  | Overstrain Failure        |
| RNF  | Random Failure            |

---

## Project Workflow

```text
Dataset Collection
        ↓
Data Cleaning & Validation
        ↓
Failure Analysis
        ↓
Timestamp Generation
        ↓
External Context Generation (Ambient Temp, Humidity, Load, Shift, Day Type)
        ↓
Contextual Data Fusion (Left Join on timestamp)
        ↓
Dataset Validation
        ↓
Feature Engineering (Temperature Diff, Load Ratio, Shift/Day Encoding)
        ↓
Correlation Analysis
        ↓
Class Imbalance Analysis (SMOTE)
        ↓
Stratified 5-Fold Cross Validation
        ↓
LightGBM Model Training & Evaluation
        ↓
Model Export (model.pkl + encoders.pkl)
        ↓
Flask Web Application Development
        ↓
Authentication System (SQLite + Werkzeug)
        ↓
Prediction Dashboard & Result Visualization
        ↓
Personalized History & CSV Export
        ↓
✅ Production-Ready Predictive Maintenance System
```

---

## Weekly Progress Summary

### Week 1 — Data Preparation & Validation ✅
- Dataset loading and inspection
- Missing value analysis (0 missing values found)
- Duplicate record detection (0 duplicates found)
- Data type validation
- Failure category analysis (TWF, HDF, PWF, OSF, RNF)
- Identifier removal (UDI, Product ID)
- Cleaned dataset: `preprocessed_ai4i2020.csv`

### Week 2 — Contextual Data Integration ✅
- Timestamp generation → `timestamps_added.csv`
- Synthetic contextual dataset generation → `external_context.csv`
  - Ambient Temperature, Load Density, Humidity, Shift, Day Type
- Timestamp-based left join → `contextual_merged_dataset.csv`
- Post-merge validation (0 missing, 0 duplicates)
- Feature engineering:
  - Temperature Difference = Process Temp − Ambient Temp
  - Load Ratio = Current Load / Max Load
  - Shift & Day Type encoding
- Correlation analysis

### Week 3 — Model Development & Evaluation ✅
- Stratified 5-Fold Cross Validation implementation
- Class imbalance analysis
- SMOTE applied inside each CV fold (prevents data leakage)
- LightGBM model training and evaluation
- Model serialization: `model.pkl` + `encoders.pkl`
- Fold-wise accuracy, mean accuracy, standard deviation reported
- Stable cross-validation results with low variance

### Week 4 — Full-Stack Flask Application ✅
- Secure user authentication (Signup / Login / Logout)
- Password hashing with Werkzeug bcrypt
- `login_required` route protection decorator
- Premium dark glassmorphism UI (Bootstrap 5.3 + custom CSS)
- 11-feature prediction form with 4 grouped sections
- Real-time LightGBM prediction with confidence % and risk level
- Animated results page with pulsing color-coded borders
- Personalized prediction history (per-user filtered view)
- Live client-side search on history table
- Personalized CSV download (user's records only, in-memory filter)
- Auto-creating prediction history CSV with header repair logic
- Sticky navbar, dismissible flash alerts, team footer

---

## Security Features

| Feature                        | Implementation                       |
|--------------------------------|--------------------------------------|
| Password hashing               | Werkzeug `generate_password_hash`    |
| Plain password never stored    | Only bcrypt hash in SQLite           |
| Route protection               | `@login_required` decorator          |
| Session management             | Flask session with secret key        |
| Duplicate email prevention     | SQLite `UNIQUE` constraint + flash   |
| Invalid login handling         | Flash message, no details leaked     |
| Missing model handling         | RuntimeError on startup              |
| Invalid input handling         | KeyError / ValueError caught + flash |
| Missing CSV handling           | Auto-created with header on demand   |

---

## Final Project Status

### ✅ Completed

| Phase | Task |
|-------|------|
| Data  | Dataset Collection |
| Data  | Data Cleaning & Validation |
| Data  | Missing Value & Duplicate Analysis |
| Data  | Failure Category Analysis |
| Data  | Timestamp Generation |
| Data  | Contextual Dataset Generation |
| Data  | Contextual Data Fusion |
| Data  | Post-Merge Validation |
| Data  | Feature Engineering |
| Data  | Correlation Analysis |
| Model | Class Imbalance Analysis |
| Model | SMOTE Implementation |
| Model | Stratified K-Fold CV |
| Model | LightGBM Training & Evaluation |
| Model | Model Export (pkl files) |
| App   | Flask Application Setup |
| App   | User Authentication (Signup/Login/Logout) |
| App   | Password Hashing & Security |
| App   | Prediction Dashboard (11-feature form) |
| App   | LightGBM Integration & Real-time Prediction |
| App   | Confidence Score & Risk Level Computation |
| App   | Animated Result Page |
| App   | Personalized Prediction History |
| App   | Live Search on History Table |
| App   | Personalized CSV Download |
| App   | Auto-creating & Self-repairing History CSV |
| App   | Premium Dark Glassmorphism UI |
| App   | Responsive Bootstrap 5.3 Design |

---

## Current Project Maturity

```
Week 1: ✅ Data Preparation & Validation
Week 2: ✅ Contextual Data Fusion & Feature Engineering
Week 3: ✅ Cross Validation, SMOTE & LightGBM Model Development
Week 4: ✅ Full-Stack Flask Web Application (Auth + Dashboard + History)
```

---

## Expected Outcome

The final AI-powered Predictive Maintenance System leverages machine telemetry data and contextual environmental information to predict machine failures before they occur. The system reduces downtime, optimizes maintenance schedules, improves operational efficiency, and supports intelligent, data-driven maintenance decisions in industrial manufacturing and automotive environments — delivered through a secure, authenticated, production-quality web dashboard.
