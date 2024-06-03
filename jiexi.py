import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# Create DataFrame from given data
data = {
    'Case': ['ibmpg1', 'ibmpg2', 'ibmpg3', 'ibmpg4', 'ibmpg5', 'ibmpg6'],
    'Time': [0.358, 1.466, 12.204, 13.082, 13.5, 21.739],
    'Memory': [9.171875, 43.96875, 357.695312, 359.699219, 354.058594, 642.332031],
    'Node': [30638, 127238, 851584, 953583, 1079310, 1670494]
}

df = pd.DataFrame(data)

# Normalize the data
scaler = MinMaxScaler()
normalized_df = pd.DataFrame(scaler.fit_transform(df[['Time', 'Memory', 'Node']]),
                             columns=['Time', 'Memory', 'Node'])

# Plotting the normalized data
# Adjusting the plot to have a more professional, research-oriented appearance using muted colors
plt.figure(figsize=(10, 6))
colors = ['navy', 'darkgreen', 'maroon']  # Professional color palette
lines = ['-', '-', ':']  # Different line styles for clarity

for i, column in enumerate(normalized_df.columns):
    plt.plot(df['Case'], normalized_df[column], marker='o', label=column, color=colors[i], linestyle=lines[i])

plt.title('')
plt.xlabel('Case')
plt.ylabel('Normalized Values')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

plt.savefig("jiexi.png")
