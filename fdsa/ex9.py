import math 
import numpy as np 
from numpy.random import randn 
from statsmodels.stats.weightstats import ztest 
mean_iq = 110 
sd_iq = 15/math.sqrt(5) 
alpha =0.05 
null_mean =100 
print(randn(5)) 
data = sd_iq*randn(5)+mean_iq 
print(data) 
print('mean=%.2f stdv=%.2f' % (np.mean(data), np.std(data))) 
ztest_Score, p_value= ztest (data, value = null_mean, alternative='larger') 
print(ztest_Score) 
print(p_value) 
if(p_value < alpha): 
 print("Reject Null Hypothesis") 
else: 
 print("Retain NULL Hypothesis") 