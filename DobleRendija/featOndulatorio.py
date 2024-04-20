from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import minimize
import pandas as pd

laserDoble = "DobleRendija\Laser2rendijas.xlsx"
laser2df = pd.read_excel(laserDoble)
print(laser2df)
laser2X = laser2df.iloc[int(0.1 * len(laser2df)):int(0.9 * len(laser2df)), 0].values
laser2V = laser2df.iloc[int(0.1 * len(laser2df)):int(0.9 * len(laser2df)), 1].values

# Define the equation
def intensity(params, x):
    A, C, D, X0 = params
    return A * np.cos(D*(x - X0))**2 * (np.sin(C*(x - X0))/(C*(x-X0)))**2

# Define the loss function
def loss(params, x, observed):
    predicted = intensity(params, x)
    return np.mean((predicted - observed) ** 2)

# Initial guess for parameters
initial_guess = [1, 1, 1, 1]  # Adjust as needed

# Minimize the loss function to find the best parameters
result = minimize(loss, initial_guess, args=(laser2X, laser2V),method='Nelder-Mead')

# Extract the best parameters
best_params = result.x
print("Best Parameters:", best_params)

#modelo
Y = intensity(best_params, laser2X)

plt.scatter(laser2X, laser2V, label='Original Data')
plt.plot(laser2X, Y, color='red', label='Fitted Curve')
plt.xlabel('X')
plt.ylabel('Intensity')
plt.legend()
plt.show()