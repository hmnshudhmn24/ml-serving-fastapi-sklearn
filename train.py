from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
import joblib

# Train sample model
X, y = load_iris(return_X_y=True)
model = RandomForestClassifier()
model.fit(X, y)

# Save model
joblib.dump(model, "model/model.pkl")
