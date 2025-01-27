import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from models.custom_model import CustomModel

# Load dataset
data = pd.read_csv('data/dataset.csv')
X = data.drop('target', axis=1)
y = data['target']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the custom model
model = CustomModel(param1=10, param2=20)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy*100:.2f}%")
