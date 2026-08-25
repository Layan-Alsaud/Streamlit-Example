# train_model.py
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# 1. Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# 2. Split into train/test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 4. Check accuracy (optional)
accuracy = model.score(X_test, y_test)
print(f"Model trained with accuracy: {accuracy:.2f}")

# 5. Save the model using joblib
joblib.dump(model, 'iris_model.pkl')
print("Model saved as iris_model.pkl")