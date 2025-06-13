import numpy as np
import joblib
import os

script_directory = os.path.dirname(os.path.abspath(__file__))
models_directory = os.path.join(script_directory, "Models")
disease_models = {
    "diabetes": joblib.load(os.path.join(models_directory, "diabetes.model")),
    "heart_disease": joblib.load(os.path.join(models_directory, "heart_disease.model")),
    "parkinsons": joblib.load(os.path.join(models_directory, "parkinsons.model")),
    }

def detect_disease(input_values, disease):
    input_values = np.asarray(input_values).reshape(1, -1)
    prediction = disease_models[disease].predict(input_values)
    
    return prediction[0]
