import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv('houseprices.csv')

# Handle missing values in 'bedrooms' by filling with median
df['bedrooms'] = df['bedrooms'].fillna(df['bedrooms'].median())

# Identify categorical columns and apply one-hot encoding
object_cols = df.select_dtypes(include=['object']).columns
df = pd.get_dummies(df, columns=object_cols, drop_first=True)

X = df.drop(columns=['price'])  # Features
Y = df['price']  # Target variable

reg = LinearRegression()
reg.fit(X, Y)

print("Coefficients:", reg.coef_)
print("Intercept:", reg.intercept_)

# Make a prediction
# Ensure input_data matches the transformed feature set
input_data = {
    'area': 3000,
    'bedrooms': 3,
    'bathrooms': 2,
    'stories': 1,
    'parking': 0,
    'mainroad_yes': 1,
    'guestroom_yes': 0,
    'basement_yes': 0,
    'hotwaterheating_yes': 0,
    'airconditioning_yes': 1,
    'prefarea_yes': 0,
    'furnishingstatus_semi-furnished': 0,
    'furnishingstatus_unfurnished': 1
}

# Convert input_data to DataFrame with the same columns as X
input_df = pd.DataFrame([input_data])

# Ensure all missing columns from training data are added with default 0
for col in X.columns:
    if col not in input_df:
        input_df[col] = 0

# Reorder columns to match training data
input_df = input_df[X.columns]

# Predict the price
predicted_price = reg.predict(input_df)
print("Predicted Price:", predicted_price[0])
