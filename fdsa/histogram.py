import matplotlib.pyplot as plt
import numpy as np
a = np.random.randint(60, 90, 30)
print("a=",a)
fig, ax = plt.subplots(figsize=(10, 7))
ax.hist(a, bins=[60, 65, 70, 75, 80, 85, 90])
plt.show()