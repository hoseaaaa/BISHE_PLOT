import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {

    'Model': ['1','2','3','4','5','6'],
    'PB': [97.86, 95.26, 94.60, 94.86, 91.66, 91.14],
    'P/Pmax': [83.81,84.45,74.68,73.59,75.89,74.37]
}


df = pd.DataFrame(data)

# Plotting configurations
fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.35
r1 = range(len(df))
r2 = [x + bar_width for x in r1]

# Colors for highlighting Model2
colors_pb = ['skyblue' ]
colors_ppmax = ['lightgreen' ]
ax.axhline(y=80, color='r', linestyle='--', label='Threshold (80%)')


# Bars with Model2 highlighted
ax.bar(r1, df['PB'], color=colors_pb, width=bar_width, edgecolor='grey', label='PB (%)')
ax.bar(r2, df['P/Pmax'], color=colors_ppmax, width=bar_width, edgecolor='grey', label='P/Pmax (%)')

# Adjustments to layout
ax.set_xlabel('Model', fontweight='bold')
ax.set_ylabel('Percentage', fontweight='bold')
ax.set_title('')
ax.set_xticks([r + bar_width/2 for r in range(len(df))])
ax.set_xticklabels(df['Model'])
ax.set_ylim(60, 100)  # Setting the lower limit of y-axis to 60
ax.legend()

# Show the plot
plt.tight_layout()
plt.show()

plt.savefig("jingzhundu.png")
