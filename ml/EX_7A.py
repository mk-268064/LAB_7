import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

# Load and clean data
df = pd.read_csv("7A.csv")
df.drop(['PassengerId','Name','SibSp','Parch','Ticket','Cabin','Embarked'], axis=1, inplace=True)
df['Age'].fillna(df['Age'].mean(), inplace=True)

# Encode gender
df['Gender'] = df['Gender'].map({'female': 1, 'male': 0})

# Features and target
X = df.drop('Survived', axis=1)
y = df['Survived']

# Train-test split and model training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
model = GaussianNB().fit(X_train, y_train)

# Evaluate and predict
print("Model Accuracy:", model.score(X_test, y_test))
print("Predictions:", model.predict(X_test[:10]))
print("Probabilities:\n", model.predict_proba(X_test[:10]))
