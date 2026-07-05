import joblib
import pandas as pd

# Load trained model
model = joblib.load("models/model.pkl")

# Load encoders
encoders = joblib.load("models/encoders.pkl")


def predict_machine(data):

    # Convert dictionary to DataFrame
    df = pd.DataFrame([data])

    # Encode categorical features
    categorical_columns = [
        "Type",
        "Shift",
        "Day_Type"
    ]

    for col in categorical_columns:
        df[col] = encoders[col].transform(df[col])

    # Predict
    prediction = model.predict(df)[0]

    probability = model.predict_proba(df)[0][1]

    return prediction, probability