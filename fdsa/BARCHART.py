import matplotlib.pyplot as plt 
x1 = [1, 3, 4 ] 
y1 = [4, 6, 3 ] 
x2 = [2, 4, 5] 
y2 = [5, 2, 1] 
plt.bar(x1, y1, label="Blue Bar", color='b') 
plt.bar(x2, y2, label="Green Bar", color='g') 
plt.plot() 
plt.xlabel("bar number") 
plt.ylabel("bar height") 
plt.title("Bar Chart Example") 
plt.legend() 
plt.show() 