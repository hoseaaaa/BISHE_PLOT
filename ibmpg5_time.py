
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.nonparametric.smoothers_lowess import lowess

# Data
theta = [0,0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1,0.11,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19,0.2,0.21,0.22,0.23,0.24,0.25,0.26,0.27,0.28,0.29,0.3,0.31,0.32,0.33,0.34,0.35,0.36,0.37,0.38,0.39,0.4,0.41,0.42,0.43,0.44,0.45,0.46,0.47,0.48,0.49,0.5,0.51,0.52,0.53,0.54,0.55,0.56,0.57,0.58,0.59,0.6,0.61,0.62,0.63,0.64,0.65,0.66,0.67,0.68,0.69,0.7,0.71,0.72,0.73,0.74,0.75,0.76,0.77,0.78,0.79,0.8,0.81,0.82,0.83,0.84,0.85,0.86,0.87,0.88,0.89,0.9,0.91,0.92,0.93,0.94,0.95,0.96,0.97,0.98,0.99,1]
t =[1.901,1.799,1.627,1.417,1.342,1.54,1.486,1.254,1.308,1.479,1.298,1.28,1.19,1.158,1.127,1.138,1.175,1.319,1.293,1.233,1.414,1.634,2.63,2.849,2.865,2.978,3.008,3.961,5.919,4.33,4.265,5.498,6.276,5.971,5.313,5.35,5.462,8.041,5.637,5.665,5.699,8.506,6.204,6.86,6.239,6.64,8.194,7.32,8.131,10.39,7.64,7.621,8.561,7.741,8.819,8.19,15.023,10.004,8.758,9.325,9.548,17.605,11.142,12.084,10.844,9.434,9.886,10.589,15.819,12.048,10.157,9.721,14.365,9.749,14.187,9.517,10.297,10.389,10.268,16.701,11.363,11.941,16.021,12.776,14.941,13.737,12.577,14.121,10.736,10.166,10.425,12.457,14.296,10.388,10.613,14.003,17.09,11.744,7.462,10.685,9.57]
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

plt.savefig("ibmpg5_time.png")
