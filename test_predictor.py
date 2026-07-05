from utils.predictor import predict_machine

sample = {

    "Type": "L",

    "Air_temperature_K": 298.1,

    "Process_temperature_K": 308.6,

    "Rotational_speed_rpm": 1551,

    "Torque_Nm": 42.8,

    "Tool_wear_min": 0,

    "Ambient_Temperature": 29.5,

    "Load_Density": 0.65,

    "Humidity": 62,

    "Shift": "Morning",

    "Day_Type": "Weekday"

}

prediction, probability = predict_machine(sample)

print("Prediction :", prediction)

print("Probability :", probability)