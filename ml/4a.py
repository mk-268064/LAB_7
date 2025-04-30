import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Sigmoid function definition
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Expanded dataset: Age vs. Purchase (1 = Bought, 0 = Not Bought)
data = {
    'Age': [18, 20, 22, 25, 28, 30, 35, 40, 45, 47, 50, 52, 54, 56, 58, 60, 62, 65, 67, 70, 75],
    'Bought_Insurance': [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
}
df = pd.DataFrame(data)

# Splitting data
X = df[['Age']]
y = df['Bought_Insurance']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Compute sigmoid values for a range of ages
ages = np.linspace(df['Age'].min(), df['Age'].max(), 100)  # Generate 100 age values
z = model.intercept_ + model.coef_ * ages.reshape(-1, 1)  # Linear equation z = β0 + β1 * X
sigmoid_values = sigmoid(z)  # Apply sigmoid function

# Plot actual data points
plt.scatter(df.Age, df.Bought_Insurance, marker="+", color='blue', label="Actual Data")

# Plot sigmoid function
plt.plot(ages, sigmoid_values, color='red', linewidth=2, label="Sigmoid Curve")

# Labels and legend
plt.xlabel("Age")
plt.ylabel("Purchase Probability")
plt.legend()
plt.show()

print(f"Model Accuracy: {accuracy:.2f}")
