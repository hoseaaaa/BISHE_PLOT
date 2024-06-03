import matplotlib.pyplot as plt

# Data from the user input
theta_values = [0.25, 0.5, 0.75]
ibmpg1 = [0.081, 0.091, 0.095]
ibmpg2 = [0.32, 0.966, 1.365]
ibmpg3 = [3.61, 10.98, 13.01]
ibmpg4 = [4.539, 12.927, 13.201]
ibmpg5 = [4.717, 7.348, 9.004]
ibmpg6 = [15.851, 16.922, 21.008]

# Labels for the x-axis
ibm_labels = ['ibmpg1', 'ibmpg2', 'ibmpg3', 'ibmpg4', 'ibmpg5', 'ibmpg6']

# Create a figure and a set of subplots
plt.figure(figsize=(10, 6))

# Plotting each series
for i, theta in enumerate(theta_values):
    # Create a list of times for the current theta
    times = [ibmpg1[i], ibmpg2[i], ibmpg3[i], ibmpg4[i], ibmpg5[i], ibmpg6[i]]
    
    # Plot the line with label for the current theta
    plt.plot(ibm_labels, times, label=f'θ={theta}', marker='o')

# Adding the title and labels
plt.title('Time t vs IBM Systems')
plt.xlabel('IBM Systems')
plt.ylabel('Time t')

# Adding the legend
plt.legend()

# Show the plot
plt.savefig("tmp.png")
