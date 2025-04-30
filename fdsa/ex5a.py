import pandas as pd

# Series Data
Data = pd.Series([1,1,1,1,2,3,3,3,3,3,4,4,4,5])
print(Data.value_counts(sort=False))

# DataFrame
df = pd.DataFrame({'Grade': ['A', 'B', 'C', 'D', 'D'], 'Age': [18, 20, 18, 19, 19], 'Gender': ['M', 'M', 'F', 'M', 'M']})
print(df)
print(pd.crosstab(df['Grade'], 'count'))
print(pd.crosstab(df['Age'], 'count'))

# Relative Frequency Distribution
tab = pd.crosstab(df['Age'], 'count')
print(tab / tab.sum())

print(pd.crosstab(df['Age'], df['Grade']))
