import matplotlib.pyplot as plt
import numpy as np

# Define the range for the input values
x = np.linspace(-5, 5, 200)

# Activation functions
sigmoid = 1 / (1 + np.exp(-x))
tanh = np.tanh(x)
relu = np.maximum(0, x)
softplus = np.log(1 + np.exp(x))

# Plotting the functions
plt.figure(figsize=(10, 6))
plt.plot(x, sigmoid, label='sigmoid', color='blue')
plt.plot(x, tanh, label='tanh', color='green')
plt.plot(x, relu, label='ReLU', color='red')
plt.plot(x, softplus, label='softplus', color='cyan')

# Adding labels and title
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Comparison of Activation Functions')
plt.legend()
plt.grid(True)
plt.savefig("relu.png")
