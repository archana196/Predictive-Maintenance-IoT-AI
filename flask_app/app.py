from flask import Flask, render_template, request
import joblib
import os

# Initialize Flask app
app = Flask(__name__)

# Load LightGBM model
MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "model",
    "model.pkl"
)

model = joblib.load(MODEL_PATH)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    type_value = int(request.form["Type"])

    air_temp = float(request.form["Air_temperature_K"])
    process_temp = float(request.form["Process_temperature_K"])
    rotational_speed = float(request.form["Rotational_speed_rpm"])
    torque = float(request.form["Torque_Nm"])
    tool_wear = float(request.form["Tool_wear_min"])

    twf = int(request.form["TWF"])
    hdf = int(request.form["HDF"])
    pwf = int(request.form["PWF"])
    osf = int(request.form["OSF"])
    rnf = int(request.form["RNF"])

    timestamp = float(request.form["timestamp"])

    ambient_temp = float(request.form["Ambient_Temperature"])
    load_density = float(request.form["Load_Density"])
    humidity = float(request.form["Humidity"])

    shift = int(request.form["Shift"])
    day_type = int(request.form["Day_Type"])

    # Engineered features
    temp_diff = process_temp - air_temp
    load_ratio = load_density / 100
    humidity_impact = humidity * ambient_temp

    features = [[
        type_value,
        air_temp,
        process_temp,
        rotational_speed,
        torque,
        tool_wear,
        twf,
        hdf,
        pwf,
        osf,
        rnf,
        timestamp,
        ambient_temp,
        load_density,
        humidity,
        shift,
        day_type,
        temp_diff,
        load_ratio,
        humidity_impact
    ]]

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