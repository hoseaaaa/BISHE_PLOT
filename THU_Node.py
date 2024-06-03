import matplotlib.pyplot as plt

# Given data for the new experiment
cases = [
        'thupg1','thupg2','thupg3','thupg4','thupg5','thupg6']
nodes = [4974439,8989132,11778121,15209208,19231049,23505915
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
plt.savefig("thu_Node.png")  # 保存第二张图
