import numpy as np
import matplotlib.pyplot as plt

# Simulating some data for demonstration purposes
np.random.seed(0)
x = np.random.rand(1000) * 0.5
y = x + np.random.normal(0, 0.02, size=x.shape)

# Plotting the figure
plt.figure(figsize=(8, 6))
plt.scatter(x, y, alpha=0.5)

# Plotting the identity line
plt.plot([0, 0.5], [0, 0.5], 'k--', label='y = x')

plt.xlabel('Predicted Delay (ns)')
plt.ylabel('Actual Delay (ms)')
plt.title('')
plt.legend()
plt.savefig("cnn_result.png")
