import matplotlib.pyplot as plt

# Given data
cases = ['ibmpg1', 'ibmpg2', 'ibmpg3', 'ibmpg4', 'ibmpg5', 'ibmpg6']
time = [0.358, 1.466, 12.204, 13.082, 13.5, 21.739]
memory = [9.171875, 43.96875, 357.695312, 359.699219, 354.058594, 642.332031]

# Create figure and axis objects with subplots()
fig, ax1 = plt.subplots()

# Line chart for Time
ax1.set_xlabel('Case')
ax1.set_ylabel('Time (s)', color='tab:red')
line1 = ax1.plot(cases, time, color='tab:red', marker='o', label='Time (s)')

# Create a second y-axis for the Memory data with the same x-axis
ax2 = ax1.twinx()  
ax2.set_ylabel('Memory (MB)', color='tab:blue')
line2 = ax2.plot(cases, memory, color='tab:blue', marker='s', label='Memory (G)')

# Combine the legends
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc=0)

# Set the title of the graph
plt.title('')

# Show plot
plt.savefig("Parse.png")

