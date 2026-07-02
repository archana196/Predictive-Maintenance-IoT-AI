from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained LightGBM model
model = joblib.load("model/model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    features = [
        float(request.form["air_temp"]),
        float(request.form["process_temp"]),
        float(request.form["rotational_speed"]),
        float(request.form["torque"]),
        float(request.form["tool_wear"]),
        float(request.form["ambient_temp"]),
        float(request.form["load_density"]),
        float(request.form["humidity"])
    ]

    data = np.array(features).reshape(1, -1)

    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0]

    confidence = max(probability) * 100

    status = "Healthy" if prediction == 0 else "Failure"

    return render_template(
        "result.html",
        status=status,
        confidence=round(confidence, 2)
    )


if __name__ == "__main__":
    app.run(debug=True)