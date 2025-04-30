import matplotlib.pyplot as plt 
x1 = [2, 3, 4] 
y1 = [5, 5, 5] 
x2 = [1, 2, 3] 
y2 = [2, 3, 2] 
y3 = [6, 8, 7] 
plt.scatter(x1, y1) 
plt.scatter(x2, y2, marker='v', color='r') 
plt.scatter(x2, y3, marker='^', color='m') 
plt.title('Scatter Plot Example') 
plt.show() 