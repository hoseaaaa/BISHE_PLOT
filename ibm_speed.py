import pandas as pd
import matplotlib.pyplot as plt

# Load the image data into a DataFrame
data = {
    "Benchmark": ["ibmpg1", "ibmpg2", "ibmpg3", "ibmpg4", "ibmpg5", "ibmpg6"
                  ],
    "CKTSO": [0.110, 0.823, 13.582, 17.798, 4.693, 7.967
              ],
    "ESPsim": [0.063, 2.224, 0.885, 2.051, 1.546, 1.566],
    "ANN-AMG": [0.013, 0.166, 0.821, 0.695, 0.745, 1.337]
}

df = pd.DataFrame(data)

# Plotting the data
fig, ax = plt.subplots(figsize=(12, 8))

# Set the position of bar on X axis
barWidth = 0.25
r1 = range(len(df['Benchmark']))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

# Make the plot
plt.bar(r1, df['CKTSO'], color='green', width=barWidth, edgecolor='grey', label='CKTSO')
plt.bar(r2, df['ESPsim'], color='red', width=barWidth, edgecolor='grey', label='ESPsim')
plt.bar(r3, df['ANN-AMG'], color='blue', width=barWidth, edgecolor='grey', label='ANN-AMG')

# Add xticks on the middle of the group bars
plt.xlabel('Benchmark', fontweight='bold', fontsize=15)
plt.xticks([r + barWidth for r in range(len(df['Benchmark']))], df['Benchmark'], rotation=45)
plt.ylabel('Time(s)', fontweight='bold', fontsize=15)
plt.title('Benchmark Performance', fontweight='bold', fontsize=16)

# Create legend & Show graphic
plt.legend()
plt.tight_layout()

# Save and display the plot
plt.savefig("ibm_speed.png")
