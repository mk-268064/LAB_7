
import pandas as pd
msg=pd.read_csv('7A.csv',names=['message','label'])
print('Total Instances of Dataset:',msg.shape[0])
msg['labelnum']=msg.label.map({'pos':1,'neg':0})
print(msg)
X=msg.message
y=msg.labelnum
from sklearn.model_selection import train_test_split
Xtrain,Xtest,ytrain,ytest=train_test_split(X,y)
from sklearn.feature_extraction.text import CountVectorizer