import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import joblib

# Generate synthetic dataset
np.random.seed(42)

num_samples = 1000

difficulty = np.random.randint(1, 6, num_samples)
days_left = np.random.randint(1, 15, num_samples)
past_score = np.random.randint(0, 101, num_samples)
priority = np.random.randint(1, 4, num_samples)

# Realistic formula for hours
hours_needed = (
    difficulty * 1.5 +
    (15 - days_left) * 0.3 +
    (100 - past_score) * 0.05 +
    (4 - priority) * 1.2 +
    np.random.normal(0, 0.5, num_samples)  # noise
)

# Prevent negative values
hours_needed = np.clip(hours_needed, 0.5, None)

# Create DataFrame
df = pd.DataFrame({
    "difficulty": difficulty,
    "days_left": days_left,
    "past_score": past_score,
    "priority": priority,
    "hours_needed": hours_needed
})

X = df[["difficulty", "days_left", "past_score", "priority"]]
y = df["hours_needed"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)

print(f"Model MAE: {mae:.2f} hours")

# Save model
joblib.dump(model, "study_model.pkl")

print("Improved model trained and saved successfully!")