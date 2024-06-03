import matplotlib.pyplot as plt

# Data from the user's table
levels = [0, 1, 2, 3, 4]
data = {
    "ibmpg1": [16327,4631,740, None, None],
    "ibmpg2": [126905,28493,3823,256, None],
    "ibmpg3": [850626,338099,93626,9568,1473],
    "ibmpg4": [952618,198732,18102,1008	, None],
    "ibmpg5": [540220,111029,11396,859	, None],
    "ibmpg6": [834252,185021,20651,1464	, None]
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
plt.xticks(levels,fontsize=18)
plt.legend()
plt.grid(True)
plt.savefig("sa_Corase_cross.png")


16327,4631,740
126905,28493,3823,256	
850626,338099,93626,9568,1473
952618,198732,18102,1008	
540220,111029,11396,859	
834252,185021,20651,1464	
