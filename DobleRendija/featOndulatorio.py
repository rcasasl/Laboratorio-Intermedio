from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import minimize
import pandas as pd

laserDoble = "DobleRendija\Laser2rendijas.xlsx" 
laser2df = pd.read_excel(laserDoble)
print(laser2df)
laser2X = laser2df.iloc[int(0.1 * len(laser2df)):int(0.9 * len(laser2df)), 0].values
laser2V = laser2df.iloc[int(0.1 * len(laser2df)):int(0.9 * len(laser2df)), 1].values

# modelo
def intensity(params, x):
    X0 = 5340
    A, C, D = params
    return A * np.cos(D*(x - X0))**2 * (np.sin(C*(x - X0)+1e-12)/(C*(x-X0)+1e-12))**2

# funcion de perdida
def loss(params, x, observed):
    predicted = intensity(params, x)
    return np.mean((predicted - observed) ** 2)

# Parametros estimados
initial_guess = [0.732, 0.00057, 0.00375]

# Minimizacion de la funcion de perdida por el metodo Nelder-Mead (hyperparameters)
result = minimize(loss, initial_guess, args=(laser2X, laser2V),method='Nelder-Mead')

# Sacamos los mejores parametros
best_params = result.x
print("Best Parameters:", best_params)

#valores en Y para el modelo para graficar
Y = intensity(best_params, laser2X)

plt.scatter(laser2X-5340, laser2V, label='Original Data')
plt.plot(laser2X-5340, Y, color='red', label='Fitted Curve')
plt.xlabel('X')
plt.ylabel('Voltaje')
plt.legend()
plt.show()

plt.scatter(laser2X, (Y-laser2V)/max(Y), label='Residuos', color='black')
plt.grid()
plt.xlabel('X')
plt.ylabel('Voltaje')
plt.title('Residuos')
plt.show()