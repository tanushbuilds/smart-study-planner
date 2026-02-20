import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Create sample training data
data = {
    "difficulty": [5, 3, 4, 2, 1, 5, 3, 4],
    "days_left": [2, 10, 5, 7, 14, 1, 8, 3],
    "past_score": [40, 80, 60, 75, 90, 30, 70, 50],
    "priority": [3, 2, 2, 1, 1, 3, 2, 3],  # High=3, Medium=2, Low=1
    "hours_needed": [5, 2, 3, 2, 1, 6, 3, 4]
}

df = pd.DataFrame(data)

X = df[["difficulty", "days_left", "past_score", "priority"]]
y = df["hours_needed"]

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "study_model.pkl")

print("Model trained and saved successfully!")