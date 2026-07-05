from flask import Flask, render_template, request
import joblib
import pandas as pd
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(__file__)

model = joblib.load(
    os.path.join(BASE_DIR, "model", "model.pkl")
)

encoders = joblib.load(
    os.path.join(BASE_DIR, "model", "encoders.pkl")
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    machine_type = request.form["Type"]
    shift = request.form["Shift"]
    day_type = request.form["Day_Type"]

    # Encode categorical features
    machine_type = encoders["Type"].transform([machine_type])[0]
    shift = encoders["Shift"].transform([shift])[0]
    day_type = encoders["Day_Type"].transform([day_type])[0]

    features = pd.DataFrame([{
        "Type": machine_type,
        "Air_temperature_K": float(
            request.form["Air_temperature_K"]
        ),
        "Process_temperature_K": float(
            request.form["Process_temperature_K"]
        ),
        "Rotational_speed_rpm": float(
            request.form["Rotational_speed_rpm"]
        ),
        "Torque_Nm": float(
            request.form["Torque_Nm"]
        ),
        "Tool_wear_min": float(
            request.form["Tool_wear_min"]
        ),
        "Ambient_Temperature": float(
            request.form["Ambient_Temperature"]
        ),
        "Load_Density": float(
            request.form["Load_Density"]
        ),
        "Humidity": float(
            request.form["Humidity"]
        ),
        "Shift": shift,
        "Day_Type": day_type
    }])

    prediction = model.predict(features)[0]

    probability = model.predict_proba(features)[0]
    confidence = round(max(probability) * 100, 2)

    status = "Healthy" if prediction == 0 else "Failure"

    return render_template(
        "results.html",
        status=status,
        confidence=confidence
    )


if __name__ == "__main__":
    app.run(debug=True)