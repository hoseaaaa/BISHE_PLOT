import matplotlib.pyplot as plt
import numpy as np

# Data
theta = [0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1]
t = [3.666, 2.652, 4.256, 2.472, 2.435, 2.541, 2.13, 2.243, 2.168, 2.069, 2.073]

# Convert lists to numpy arrays
theta_np = np.array(theta)
t_np = np.array(t)

# Assume a constant percentage error for illustration purposes (e.g., 10% of each t value)
errors = t_np * 0.1

# Create a scatter plot with error bars
plt.figure(figsize=(10, 6))
plt.errorbar(theta_np, t_np, yerr=errors, fmt='o', color='blue', ecolor='lightgray', capsize=5)
plt.title('Scatter Plot with Error Bars')
plt.xlabel('θ')
plt.ylabel('t')
plt.grid(True)
plt.savefig("tmp2.png")
