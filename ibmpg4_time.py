
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.nonparametric.smoothers_lowess import lowess

# Data
theta = [0,0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1,0.11,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19,0.2,0.21,0.22,0.23,0.24,0.25,0.26,0.27,0.28,0.29,0.3,0.31,0.32,0.33,0.34,0.35,0.36,0.37,0.38,0.39,0.4,0.41,0.42,0.43,0.44,0.45,0.46,0.47,0.48,0.49,0.5,0.51,0.52,0.53,0.54,0.55,0.56,0.57,0.58,0.59,0.6,0.61,0.62,0.63,0.64,0.65,0.66,0.67,0.68,0.69,0.7,0.71,0.72,0.73,0.74,0.75,0.76,0.77,0.78,0.79,0.8,0.81,0.82,0.83,0.84,0.85,0.86,0.87,0.88,0.89,0.9,0.91,0.92,0.93,0.94,0.95,0.96,0.97,0.98,0.99,1]
t=[5.749,3.3,3.146,2.994,2.862,2.758,3.425,2.741,2.555,2.542,2.774,2.611,2.544,5.568,2.639,2.61,2.575,2.328,2.741,2.538,3.478,3.534,3.331,4.018,3.54,5.587,3.425,9.579,4.233,5.007,4.575,5.762,7.467,5.942,6.279,6.926,6.303,7.313,6.421,8.313,13.324,8.822,10.239,10.427,11.247,14.648,13.888,13.62,13.013,17.333,17.304,17.912,16.842,15.292,17.672,15.387,15.148,18.486,21.691,15.777,15.457,20.59,17.224,21.947,20.122,16.642,19.29,17.135,17.407,13.192,15.743,14.67,14.297,14.392,15.026,15.872,14.11,13.351,15.079,16.816,16.425,15.434,13.538,14.497,13.682,13.87,18.72,14.789,17.148,15.117,18.39,15.656,15.788,15.875,17.764,17.509,16.597,12.117,11.853,13.063,12.334]
# Convert the lists to numpy arrays
theta_np = np.array(theta)
t_np = np.array(t)

# # Fit a cubic polynomial using the least squares method
# coefficients_3 = np.polyfit(theta_np, t_np, 4)
# polynomial_3 = np.poly1d(coefficients_3)

# # Generate theta values for plotting the regression curve
# theta_fit = np.linspace(min(theta_np), max(theta_np), 100)
# t_fit_3 = polynomial_3(theta_fit)

# # Plotting the scatter plot and the cubic regression curve
# plt.figure(figsize=(10, 6))
# plt.scatter(theta_np, t_np, color='blue', label='Data Points')  # Scatter plot of the original data
# plt.plot(theta_fit, t_fit_3, color='purple', label='Regression Curve')  # Cubic regression curve
# plt.title('')
# plt.xlabel('θ')
# plt.ylabel('t')
# plt.legend()
# plt.grid(True)
# plt.savefig("ibmpg5_time.png")

# # Print the coefficients of the cubic polynomial
# print("Cubic polynomial coefficients:", coefficients_3)



# Calculate the LOWESS smoothed line
lowess_result = lowess(t_np, theta_np, frac=0.3) # frac is the fraction of data used to compute each y-value

# Extract the LOWESS smoothed values
theta_lowess, t_lowess = lowess_result[:, 0], lowess_result[:, 1]

# Plotting the scatter plot with the LOWESS smoothed line
plt.figure(figsize=(10, 6))
plt.scatter(theta_np, t_np, color='blue', label='Data Points')
plt.plot(theta_lowess, t_lowess, color='red', label='LOWESS Curve')
plt.title('')
plt.xlabel('θ')
plt.ylabel('t')
plt.legend()
plt.grid(True)
plt.show()

plt.savefig("ibmpg4_time.png")




