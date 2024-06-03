# Given data
import numpy as np
import matplotlib.pyplot as plt

run_times = [
    2.228, 2.247, 2.2, 2.06, 2.09, 2.327, 2.385, 2.236, 2.216, 2.279,
    2.118, 2.125, 2.314, 2.394, 2.295, 2.306, 2.166, 2.185, 2.079, 4.363,
    2.32, 5.022, 2.213, 2.247, 2.202, 2.294, 2.354, 3.031, 2.288, 2.212,
    2.504, 2.236, 2.234, 2.306, 2.37, 2.145, 2.091, 2.288, 2.793, 2.25,
    3.032, 8.138, 2.344, 2.096, 2.287, 6.465, 2.17, 2.866, 2.154, 2.174,
    2.546, 2.117, 2.052, 2.045, 2.209, 2.238, 2.238, 2.485, 2.767, 4.126,
    2.965, 2.429, 5.186, 2.279, 2.113, 2.111, 2.45, 2.225, 2.481, 2.127,
    2.128, 2.126, 7.149, 2.424, 2.391, 2.24, 2.255, 2.098, 2.206, 2.052,
    2.093, 2.954, 2.128, 2.182, 2.151, 2.044, 2.065, 2.327, 2.484, 2.59,
    2.106, 2.73, 2.323, 2.304, 2.18, 2.039, 2.086, 2.264, 2.149, 2.312
]

# Let's calculate the mean and standard deviation
mean_run_time = np.mean(run_times)
std_dev_run_time = np.std(run_times)

# We'll consider data points that lie beyond 2 standard deviations from the mean as outliers
outlier_threshold = mean_run_time + 2 * std_dev_run_time

# Prepare the plot
plt.figure(figsize=(10,6))
plt.scatter(range(len(run_times)), run_times, color='blue')

# Plot a horizontal line at the outlier threshold
plt.axhline(y=outlier_threshold, color='r', linestyle='--', label=f'Outlier Threshold: {outlier_threshold:.3f}')

# Annotate the outliers
for i, run_time in enumerate(run_times):
    if run_time > outlier_threshold:
        plt.annotate(f'  {run_time}', (i, run_time), textcoords="offset points", xytext=(0,10), ha='center', color='red')

# Adding title and labels
plt.title('')
plt.xlabel('Run Number')
plt.ylabel('Time (seconds)')
plt.legend()

# Show the plot with outliers marked
plt.savefig("run_time.png")

# Return the analysis of the situation based on the mean and standard deviation
(mean_run_time, std_dev_run_time, outlier_threshold)
