from flask import Flask, render_template, request
from utils.predictor import predict_machine

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

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

    prediction, probability = predict_machine(data)

    if prediction == 1:

        result = "⚠️ Machine Failure Predicted"

        color = "danger"

    else:

        result = "✅ Machine is Healthy"

        color = "success"

    return render_template(

        "result.html",

        prediction=result,

        probability=round(probability * 100, 4),

        color=color

    )


if __name__ == "__main__":

    app.run(debug=True)