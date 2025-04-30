print("1.Reading data from a text file")
T = open(r'Data.txt')
print(T.read())

print("--------------------------------------------------------------------")
print("2.Reading the CSV file")
import pandas as pd
data = pd.read_csv(r'Data.csv')
print(data)


print("--------------------------------------------------------------------")
print("3.Reading the excel file")

import pandas as pd
data = pd.read_excel(r'ds.xlsx')
print(data)


print("--------------------------------------------------------------------")
print("4.Reading from web")

import pandas as pd 
url="https://en.wikipedia.org/wiki/Demon_Slayer:_Kimetsu_no_Yaiba" 
df=pd.read_html(url) 
print(df)


print("--------------------------------------------------------------------")


