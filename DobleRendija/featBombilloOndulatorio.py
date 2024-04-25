from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import minimize
import pandas as pd

laserDoble = "DobleRendija\dobleRendijaBombillo.xlsx"
laser2df = pd.read_excel(laserDoble)
print(laser2df)
laser2X = laser2df.iloc[int(0 * len(laser2df)):int(1 * len(laser2df)), 0].values
laser2V = laser2df.iloc[int(0 * len(laser2df)):int(1 * len(laser2df)), 4].values

# modelo
def intensity(params, x):
    X0 = 1600
    A, C, D = params
    return A * np.cos(D*(x - X0))**2 * (np.sin(C*(x - X0)+1e-12)/(C*(x-X0)+1e-12))**2

# funcion de perdida
def loss(params, x, observed):
    predicted = intensity(params, x)
    return np.mean((predicted - observed) ** 2)

# Parametros estimados
initial_guess = [0.014167, 0.0007, 0.004]

# Minimizacion de la funcion de perdida por el metodo Nelder-Mead (hyperparameters)
result = minimize(loss, initial_guess, args=(laser2X, laser2V),method='Nelder-Mead')

# Sacamos los mejores parametros
best_params = result.x
print("Best Parameters:", best_params)

#valores en Y para el modelo para graficar
Y = intensity(best_params, laser2X)

plt.scatter(laser2X-1600, laser2V, label='Original Data')
plt.plot(laser2X-1600, Y, color='red', label='Fitted Curve')
plt.xlabel('X')
plt.ylabel('Conteos')
plt.legend()
plt.show()

plt.scatter(laser2X, (Y-laser2V)/max(Y), label='Residuos', color='black')
plt.grid()
plt.xlabel('X')
plt.ylabel('Conteos')
plt.title('Residuos')
plt.show()