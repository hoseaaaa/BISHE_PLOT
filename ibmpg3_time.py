
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.nonparametric.smoothers_lowess import lowess

# Data
theta = [0,0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1,0.11,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19,0.2,0.21,0.22,0.23,0.24,0.25,0.26,0.27,0.28,0.29,0.3,0.31,0.32,0.33,0.34,0.35,0.36,0.37,0.38,0.39,0.4,0.41,0.42,0.43,0.44,0.45,0.46,0.47,0.48,0.49,0.5,0.51,0.52,0.53,0.54,0.55,0.56,0.57,0.58,0.59,0.6,0.61,0.62,0.63,0.64,0.65,0.66,0.67,0.68,0.69,0.7,0.71,0.72,0.73,0.74,0.75,0.76,0.77,0.78,0.79,0.8,0.81,0.82,0.83,0.84,0.85,0.86,0.87,0.88,0.89,0.9,0.91,0.92,0.93,0.94,0.95,0.96,0.97,0.98,0.99,1]
t =[1.398641229,1.117481837,0.792518748,0.723709751,0.449431715,0.744760262,1.230303759,0.754964652,1.262450196,1.23537725,0.7248983,1.259726688,1.120450999,0.712807178,0.706209233,1.105974241,1.091259443,1.118956643,0.631557072,1.231058752,1.045209341,1.463727309,2.14306319,2.841394827,2.625366602,1.998596985,2.225585821,3.867054034,5.423235647,3.983572302,3.598755959,4.56868978,6.068169278,5.707378599,4.341489563,5.328732147,5.099866258,7.105386554,5.132329029,4.894342896,5.400218597,8.431985911,5.457187169,6.39460204,5.826379323,5.867606762,7.842824533,6.462458429,7.427922114,9.444566697,7.579669908,7.427698227,8.23303227,7.026444225,8.386128188,7.837048284,14.73898336,9.237068903,8.63347729,9.184008059,9.085581559,16.76513349,11.09203358,11.76768533,10.54171215,8.817318102,9.234221146,10.05808623,15.4747743,11.21597637,9.44057035,9.295594103,14.26805617,8.845541846,13.71550481,8.709906954,9.329044272,10.04230559,9.717384281,15.73008918,11.15034036,11.1252173,15.84509629,12.55469133,13.97740655,12.84857018,12.04087948,13.99394361,10.687457,9.891683251,10.36042725,12.03419169,13.30127429,10.20538242,9.93356811,13.40400362,16.87465189,11.07637433,6.606808608,10.47497917,9.395050155]

# [1.397736244,1.559400826,1.033558668,0.621300649,0.612103037,1.308146459,0.633927897,0.433929152,1.039912601,0.950721183,0.586772967,0.752241018,0.326107152,0.559681386,0.981459314,0.163631944,0.567493626,1.043092591,1.184657604,0.549280903,0.588804648,1.570226991,1.823047802,1.931258465,2.497555782,2.001533062,2.085464197,3.474765493,5.0161689,3.395931069,3.816452861,4.640620723,6.123622118,5.177370881,4.414090113,4.557339962,4.872332192,7.768803391,5.486041186,5.070910933,4.943555527,8.409136135,5.808386758,6.42089805,5.418106343,6.158846143,7.971808087,7.061056663,7.134358587,9.404498607,7.278140701,6.737329706,7.909229413,7.068001083,8.801666117,7.890498687,14.58845596,9.141686739,7.814624936,8.830932578,9.404142549,17.60115763,10.91820066,11.95563161,9.952117195,9.055900501,9.275247421,9.927343072,15.04158401,11.74214237,9.774966365,9.395174248,13.91145791,9.366662453,13.9498237,8.754331057,9.888510923,9.845301048,9.313336785,16.29452203,10.50817243,11.15115682,15.6280718,12.38541512,14.30444703,12.90791192,11.98588404,13.93089781,10.45529637,9.912221981,10.06105325,12.34635203,13.78925806,10.01148513,10.40151298,13.23259906,16.86190266,10.7840166,6.879969777,10.66435351,9.402742593]
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

plt.savefig("ibmpg3_time.png")




