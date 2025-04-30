print("AVERAGE AND VARIABILITY using numpy and List")
import numpy as np
list = [2, 4, 4, 4, 5, 5, 7, 9] 
print(np.average(list))
print(np.var(list))
print(np.std(list))

print("________________________________________________________________________________")

import numpy as np 
x = np.arange(5) 
print(x) 
r11 = np.mean(x) 
r12 = np.average(x) 
print("\nMean: ", r11, r12) 
r21 = np.std(x) 
r22 = np.sqrt(np.mean((x - np.mean(x)) ** 2)) 
print("\nstd dev: ", r21, r22) 
r31 = np.var(x) 
r32 = np.mean((x - np.mean(x)) ** 2) 
print("\nvariance: ", r31, r32)

print("________________________________________________________________________________")


print("AVERAGE AND VARIABILITY using numpy and Dictionary")

import numpy as np 
dicti = {'a': 20, 'b': 32, 'c': 12}
listr = [] 
for value in dicti.values(): 
 listr.append(value) 
mean=np.mean(listr) 
std = np.std(listr) 
print(mean) 
print(std)

print("________________________________________________________________________________")

print("AVERAGE AND VARIABILITY using Pandas ")

import pandas as pd 
s = pd.Series(data = [5, 9, 8, 5, 7, ]) 
print(s) 
print(s.mean()) 
print(s.std())

print("________________________________________________________________________________")

df = pd.DataFrame({'ID':[114, 345, 157788, 5626],'Discount':[10, 20, 10, 50]}) 
print(df) 
print(df.mean())
print(df.std()) 



