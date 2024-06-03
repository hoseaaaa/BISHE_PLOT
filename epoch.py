# Let's simulate a perfect training loss curve.

# Importing required libraries
import matplotlib.pyplot as plt
import numpy as np

# Epochs
epochs = np.arange(0, 500)

# Simulated perfect training loss
# Starts high, decreases rapidly, then slows down and plateaus, minimal noise
perfect_loss = np.exp(-epochs/50) + 0.01 * np.random.randn(500) * np.exp(-epochs/200)

# Creating the plot
plt.figure(figsize=(10, 5))
plt.plot(epochs, perfect_loss, label='Training Loss')

# Adding title and labels
plt.title('Simulated Perfect Training Loss Curve')
plt.xlabel('Epoch')
plt.ylabel('Loss')

# Adding a legend
plt.legend()

# Show the plot
plt.grid(True)
plt.savefig("epoch.png")
