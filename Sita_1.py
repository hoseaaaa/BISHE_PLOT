import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sita import *
from statsmodels.nonparametric.smoothers_lowess import lowess

# It looks like we had an off-by-one error in the range. Let's fix the theta array to have the same length as the normalized_levels array

# Create the scatter plot

plt.scatter(df['theta'], df['normalized_levels'], alpha=1.0, label='scatter', 
            s=20,    # 设置点的大小
            marker='.')  # 设置点的形状为圆形
# Calculate LOWESS
lowess_results = lowess(df['normalized_levels'], df['theta'], frac=0.3)

# Plot LOWESS results
plt.plot(lowess_results[:, 0], lowess_results[:, 1], color='red', label='LOWESS')

# KDE plot with the correct 'levels' parameter
sns.kdeplot(x=df['theta'], y=df['normalized_levels'], levels=5, color='blue')

# Add title and legend
plt.title('Scatter, LOWESS, and KDE')
plt.legend()
plt.grid(True)
# Show the plot
plt.savefig("Sita_1.png")
