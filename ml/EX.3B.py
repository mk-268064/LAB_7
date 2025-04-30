import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

df = pd.read_csv('homeprices.csv')

print(df.head())

df['Bedrooms'] = df['Bedrooms'].fillna(df['Bedrooms'].median())

X = df.drop(columns=['Price'])  # Features
Y = df['Price'] 
reg = LinearRegression()
reg.fit(X, Y)

print("Coefficients:", reg.coef_)
print("Intercept:", reg.intercept_)
input_data = pd.DataFrame([[3000, 3, 40]], columns=X.columns)  # Fixes the error

predicted_price = reg.predict(input_data)
print("Predicted Price:", predicted_price[0])
