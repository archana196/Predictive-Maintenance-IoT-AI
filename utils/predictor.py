import joblib
import pandas as pd

model = joblib.load("../model/model.pkl")

def predict_machine(data):
    """
    Predict machine failure.
    Input: pandas DataFrame
    Output: prediction and probability
    """
    prediction = model.predict(data)
    probability = model.predict_proba(data)

    return prediction, probability
