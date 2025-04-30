from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sn

# Load data
digits = load_digits()
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=42)

# Show first 5 images
plt.gray()
[plt.matshow(digits.images[i]) for i in range(5)]
plt.show()

# Train model & evaluate
model = LogisticRegression(max_iter=2000).fit(X_train, y_train)
print("Model Score:", model.score(X_test, y_test))

# Show example prediction
i = 67
plt.matshow(digits.images[i])
plt.show()
print(f"Actual: {digits.target[i]} | Predicted: {model.predict([digits.data[i]])[0]}")

# First 5 predictions
print("First 5 Predictions:", model.predict(digits.data[:5]))

# Confusion matrix
cm = confusion_matrix(y_test, model.predict(X_test))
sn.heatmap(cm, annot=True, cmap='Blues', fmt='d')
plt.xlabel('Predicted')
plt.ylabel('Truth')
plt.show()
