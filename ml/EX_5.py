import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Load and encode data
df = pd.read_csv("5.csv")
le = LabelEncoder()
for col in ['company', 'job', 'degree']:
    df[col] = le.fit_transform(df[col])

# Prepare data
X = df[['company', 'job', 'degree']]
y = df['salary_more_then_100k']
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Train and plot model
model = DecisionTreeClassifier().fit(x_train, y_train)
plt.figure(figsize=(12,8))
plot_tree(model, feature_names=X.columns, filled=True)
plt.show()

# Evaluate and predict
print(f"Model accuracy: {model.score(x_test, y_test)}")
print("Prediction for input [2, 1, 0]:", model.predict([[2, 1, 0]])[0])
