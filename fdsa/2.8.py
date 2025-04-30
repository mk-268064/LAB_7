import numpy as np
a = np.array([[1, 4, 2], [3, 4, 6], [0, -1, 5]])

print("Before sorting:", np.sort(a, axis=None))
print("Row-wise sort:", np.sort(a, axis=1))
print("Column-wise sort:", np.sort(a, axis=0))
