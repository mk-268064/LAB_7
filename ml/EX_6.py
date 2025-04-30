import numpy as np

# Data normalization
X = np.array([[2, 9], [1, 5], [3, 6]], dtype=float)
y = np.array([[92], [86], [89]], dtype=float) / 100
X /= np.amax(X, axis=0)

# Simple Neural Network
class NeuralNetwork:
    def __init__(self):
        self.W1 = np.random.randn(2, 3)
        self.W2 = np.random.randn(3, 1)

    def sigmoid(self, x, deriv=False):
        return x * (1 - x) if deriv else 1 / (1 + np.exp(-x))

    def feedForward(self, X):
        self.z2 = self.sigmoid(X @ self.W1)
        return self.sigmoid(self.z2 @ self.W2)

    def backward(self, X, y, output):
        d_output = (y - output) * self.sigmoid(output, True)
        d_hidden = d_output @ self.W2.T * self.sigmoid(self.z2, True)
        self.W2 += self.z2.T @ d_output
        self.W1 += X.T @ d_hidden

    def train(self, X, y, epochs=1000):
        for i in range(epochs):
            out = self.feedForward(X)
            self.backward(X, y, out)
            if i % 100 == 0:
                print(f"Epoch {i}, Loss: {np.mean((y - out) ** 2)}")

# Train and predict
NN = NeuralNetwork()
NN.train(X, y)
print("input",str(X))
print("actual_output",str(y))
print("Predicted Output:\n", NN.feedForward(X))
