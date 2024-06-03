import numpy as np
import matplotlib.pyplot as plt

# Assuming errors are normally distributed around the mean error with the specified max error as a 3-sigma event
mean_error = 1.84E-05

max_error = 4.51E-05

num_data = 16327

# Calculate the standard deviation (sigma) assuming max error represents a 3-sigma event
sigma = max_error / 3

# Generate a normal distribution of errors
np.random.seed(100)  # for reproducibility
error_data = np.random.normal(loc=mean_error, scale=sigma, size=num_data)

# Plot the histogram
plt.figure(figsize=(10, 6))
n, bins, patches = plt.hist(error_data, bins=300, alpha=0.75, color='blue')

plt.title('Error Distribution of 16327 Data Points')
plt.xlabel('Error')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()

# Save the plot to a file
histogram_filename = 'histogram.png'
plt.savefig(histogram_filename)
