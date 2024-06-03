import matplotlib.pyplot as plt
import numpy as np

# Function to generate random data points with a trend similar to the one in the image provided
def generate_random_data_with_trend(num_points=900, num_categories=3):
    # Generating random x values (normalized ρ)
    x_values = np.random.normal(0, 1, num_points)
    
    # Generating corresponding y values (normalized t) with a slight trend
    y_values = 1.5* x_values + np.random.normal(0, 0.8, num_points)
    
    # Assigning categories based on 'h' values, for color coding in the plot
    categories = np.random.choice(range(num_categories), num_points)
    
    return x_values, y_values, categories

# Generate random data
x, y, cat = generate_random_data_with_trend()

# Plotting the data
plt.figure(figsize=(15,9))

# Using a colormap to represent different 'h' values
colormap = plt.cm.viridis

# Create a list of colors based on y values, mapped to the colormap
colors = [colormap(i) for i in np.linspace(0, 1, len(np.unique(cat)))]
theta_values = [0.75, 0.5, 0.25]

# Plot each category with different colors
for i in range(len(np.unique(cat))):
    plt.scatter(x[cat == i], y[cat == i], label=f'θ={theta_values[i]}', color=colors[i], s=10)

# Labeling the axes
plt.xlabel('normalized ρ')
plt.ylabel('normalized t')

# Adding a legend
plt.legend()

# Show the plot
plt.show()

# Show the plot
plt.show()


plt.savefig("shoulianyinzi.png")
