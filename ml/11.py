import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg

def lowess(x, y, f=0.25, iterations=3):
    n, r = len(x), int(np.ceil(f * len(x)))
    h = [np.sort(np.abs(x - x[i]))[r] for i in range(n)]
    w = (1 - np.clip(np.abs((x[:, None] - x[None, :]) / h), 0, 1) ** 3) ** 3
    yest, delta = np.zeros(n), np.ones(n)

    for _ in range(iterations):
        for i in range(n):
            W, b = delta * w[:, i], [np.sum(delta * w[:, i] * y), np.sum(delta * w[:, i] * y * x)]
            A = [[np.sum(W), np.sum(W * x)], [np.sum(W * x), np.sum(W * x * x)]]
            beta = linalg.solve(A, b)
            yest[i] = beta[0] + beta[1] * x[i]

        residuals, s = y - yest, np.median(np.abs(y - yest))
        delta = (1 - np.clip(residuals / (6.0 * s), -1, 1) ** 2) ** 2

    return yest

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x) + 0.3 * np.random.randn(100)

plt.plot(x, y, "r.", x, lowess(x, y), "b-")
plt.show()
