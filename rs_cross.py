import matplotlib.pyplot as plt

# Data from the user's table
levels = [0, 1, 2, 3, 4, 5, 6, 7]
data = {
    "ibmpg1": [16327, 7413, 957, None, None, None, None, None],
    "ibmpg2": [126905, 44621, 6768, 1600, None, None, None, None],
    "ibmpg3": [850626, 398505, 184530, 83257, 32102, 11655, 4050, 1893],
    "ibmpg4": [952618, 428595, 123848, 46917, 12559, 2740, None, None],
    "ibmpg5": [540220, 268613, 123995, 50307, 12972, 2854, None, None],
    "ibmpg6": [834252, 408322, 155078, 54015, 12550, 2907, None, None]
}

# Create the plot
plt.figure(figsize=(12, 8))
for key, values in data.items():
    # Replace None with NaN to handle missing data gracefully in the plot
    clean_values = [value if value is not None else float('nan') for value in values]
    plt.plot(levels, clean_values, marker='o', label=key)

plt.title('')
plt.xlabel('Level')
plt.ylabel('Value')
plt.xticks(levels)
plt.legend()
plt.grid(True)
plt.savefig("Corase_cross.png")
