import joblib
import numpy as np

# Load trained model
model = joblib.load("study_model.pkl")

def predict_hours(difficulty, days_left, past_score, priority):
    # Convert inputs into 2D array (model expects 2D)
    features = np.array([[difficulty, days_left, past_score, priority]])
    
    prediction = model.predict(features)
    
    return round(prediction[0], 2)