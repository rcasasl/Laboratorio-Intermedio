import matplotlib.pyplot as plt
import numpy as np
from linregress_w import linregress_w as linr


Corriente = np.array([0.15,0.65,1.15,1.65,2.15,2.65,3.15])*-1
CampoM = np.array([2.4,13.3,24.2,32.7,43.7,55.2,64.9])
Niquel = np.array([0,1,2,3,4,6,11])
Hierro = np.array([0,-2,-3,-2,-1,-1,0])
Cobre = np.array([0,0,0,0,0,0,0])

def dL(n):
    return n*6.32e-7/2

def D(n):
    return dL(n)/0.142

#CAMPO MAGNETICO VS CORRIENTE

plt.xlabel('Corriente (A)')
plt.ylabel('Campo Magnetico B(T)')
x = Corriente
y = CampoM
dy = np.array([0.0001386]*len(Corriente))
lin_reg = linr(x,y,dy)
f= lambda x: lin_reg.slope()*x+lin_reg.intercept()

x_p= np.linspace(min(x),max(x),500)


plt.scatter(x,y,c="r")
plt.grid()
plt.errorbar(x, y, yerr= dy, linestyle="")


plt.plot(x_p,f(x_p),c="k",linestyle="--")


mu = lin_reg.slope()

print("La pendiente es de: ",lin_reg.slope(),"$\pm$",lin_reg.err_slope())
print("El intercepto es de: ", lin_reg.intercept(),"$\pm$",lin_reg.err_intercept())
print("y = x",lin_reg.slope(),"$\pm$",lin_reg.err_slope(), "+",lin_reg.intercept(),"$\pm$",lin_reg.err_intercept() )

plt.show()

#RESIDUOS DE CAMPO MAGNETICO VS CORRIENTE

plt.scatter(x, (y-f(x)), label='Residuos', color='black')
plt.grid()
plt.xlabel('Corriente (A)')
plt.ylabel('Campo Magnetico B(T)')
plt.show()

#CAMPO MAGNETICO VS NIQUEL

x = Corriente
plt.plot(f(x), D(Niquel), label='Niquel')
plt.xlabel('Campo magnetico B(T)')
plt.ylabel('Δl/l0 del Niquel')
plt.grid()
plt.show()

#CAMPO MAGNETICO VS HIERRO

x = Corriente
plt.plot(f(x), D(Hierro), label='Hierro')
plt.xlabel('Campo magnetico B(T)')
plt.ylabel('Δl/l0 del Hierro')
plt.grid()
plt.show()

#CAMPO MAGNETICO VS COBRE

x = Corriente
plt.plot(f(x), D(Cobre), label='Cobre')
plt.xlabel('Campo magnetico B(T)')
plt.ylabel('Δl/l0 del Cobre')
plt.grid()
plt.show()