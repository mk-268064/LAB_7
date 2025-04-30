import numpy as np
a1 = np.array([[1, 2, 3], [4, 5, 6]]) 
a2 = np.array([[7, 8, 9], [10, 11, 12]]) 
c = np.hstack((a1, a2)) 
d = np.vstack((a1, a2)) 
print("\nHorizontal stacking :\n", c) 
print("\nVertical stacking :\n", d) 