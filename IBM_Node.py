import matplotlib.pyplot as plt

# Given data for the new experiment
cases = ['ibmpg1', 'ibmpg2', 'ibmpg3', 'ibmpg4', 'ibmpg5', 'ibmpg6']
nodes = [30638, 127238, 851584, 953583, 1079310, 1670494
]

# Create a figure and axis object
fig, ax = plt.subplots()

# Plotting the line chart
ax.plot(cases, nodes, marker='o', color='green', label='Nodes')

# Set the labels and title
ax.set_xlabel('Case')
ax.set_ylabel('Node Count')
ax.set_title('')

# Show the legend
ax.legend()
plt.grid(True)

# Show the plot
plt.savefig("iBM_Node.png")  # 保存第二张图
