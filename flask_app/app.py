from flask import Flask, render_template, request
from utils.predictor import predict_machine

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:

        # -----------------------------
        # Read form inputs
        # -----------------------------

        data = {

            "Type": request.form["Type"],

            "Air_temperature_K": float(request.form["Air_temperature_K"]),

            "Process_temperature_K": float(request.form["Process_temperature_K"]),

            "Rotational_speed_rpm": float(request.form["Rotational_speed_rpm"]),

            "Torque_Nm": float(request.form["Torque_Nm"]),

            "Tool_wear_min": float(request.form["Tool_wear_min"]),

            "Ambient_Temperature": float(request.form["Ambient_Temperature"]),

            "Load_Density": float(request.form["Load_Density"]),

            "Humidity": float(request.form["Humidity"]),

            "Shift": request.form["Shift"],

            "Day_Type": request.form["Day_Type"]

        }

        # -----------------------------
        # Prediction
        # -----------------------------

        prediction, probability = predict_machine(data)

        probability = round(probability * 100, 2)

        # -----------------------------
        # Result
        # -----------------------------

        if prediction == 1:

            result = "⚠️ Machine Failure Predicted"

            color = "danger"

        else:

            result = "✅ Machine is Healthy"

            color = "success"

        # -----------------------------
        # Risk Level
        # -----------------------------

        if probability < 20:

            risk = "LOW"

        elif probability < 50:

            risk = "MEDIUM"

        else:

            risk = "HIGH"

        # -----------------------------
        # Recommendation
        # -----------------------------

        if risk == "LOW":

            recommendation = (
                "Machine is operating normally. Continue routine maintenance."
            )

        elif risk == "MEDIUM":

            recommendation = (
                "Monitor the machine closely. Preventive maintenance is recommended."
            )

        else:

            recommendation = (
                "Immediate inspection is recommended. High possibility of machine failure."
            )

        # -----------------------------
        # Render Result Page
        # -----------------------------

        return render_template(

            "result.html",

            prediction=result,

            probability=probability,

            color=color,

            risk=risk,

            recommendation=recommendation,

            data=data

        )

    except Exception as e:

        return f"<h2>Error:</h2><p>{str(e)}</p>"


@app.route("/about")
def about():

    return """
    <h2>Predictive Maintenance System</h2>
    <p>
    AI-powered machine failure prediction using
    LightGBM, Flask, and Context-Aware Features.
    </p>
    """


if __name__ == "__main__":

    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )