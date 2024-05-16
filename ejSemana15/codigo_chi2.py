import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
from scipy import interpolate as inter
from scipy import stats as st
from scipy.optimize import minimize as mini
from scipy.optimize import newton as nwt

x = np.array([0.05,0.25,0.45,0.65,0.85,1.05,1.25,1.45,1.65,1.85])
y = np.array([0.00,0.21,0.44,0.67,0.88,1.10,1.30,1.50,2.0,2.24])
dy = np.array([0.05,0.05,0.05,0.05,0.09,0.1,0.2,0.5,0.1,0.07])


#Definimmos un intervalo para minimizar
m=np.linspace(-1,5,1000)
c=np.linspace(-4,4,1000)

#Mesh que exploramos
mm,cc = np.meshgrid(m,c)
def Chi2(X,arg=(x,y)):
    m,c=X[0],X[1]
    x,y=arg[0],arg[1]
    Chi2=np.sum((y-m*x-c)**2/dy**2)
    return Chi2

#Min chi2
p_min=mini(Chi2,(2.1,-0.5))
m_min,c_min=p_min.x[0],p_min.x[1]



Chi2_min= Chi2((m_min,c_min))
def f_m(m,c=c_min,x=x,y=y,alpha=dy,contor=1):  
    return np.sum((y-(m)*x-c)**2/(alpha)**2)-Chi2_min-contor

def f_c(c,m=m_min,x=x,y=y,alpha=dy,contor=1):  
    return np.sum((y-(m)*x-c)**2/(alpha)**2)-Chi2_min-contor


def solve_Espacio_fase_m(m=m_min,c=c_min,x=x,y=y,contorno=1,alpha=dy,gmm=0.05,infer=-1,tolerancia=1e-7):
    
    cjAnterior = c
    d = 1
    mj = m
    
    while d>tolerancia:
        #loop que minimiza m

        mjAnterior = mj

        mj = nwt(f_m,mj+0.02*infer,args=(cjAnterior,x,y,alpha,contorno)) #Newton rapshon para minimizar m

        termino = 2*gmm*np.sum((y-(mj)*x-cjAnterior)/(alpha)**2)
        
        cjAnterior += termino
        
        diff=np.abs(mj-mjAnterior)

        d = diff 
    
    return mj

def solve_Espacio_fase_c(m=m_min,c=c_min,x=x,y=y,contorno=1,alpha=dy,gmm=0.0001,infer=-1,tolerancia=1e-7):
    
    mjAnterior = m
    d = 1
    cj = c
    
    while d>tolerancia:
        #loop que minimiza c

        cjAnterior = cj

        cj = nwt(f_c,cj+0.01*infer,args=(mjAnterior,x,y,alpha,contorno)) #Newton rapshon para minimizar c

        termino = 2*gmm*np.sum(x*(y-(mjAnterior)*x-cj)/(alpha)**2)
        
        mjAnterior += termino
        
        diff=np.abs(cj-cjAnterior)
        
        d = diff 
    
    return cj

print("\n")
print("Inferior:\n")
alpha_m = solve_Espacio_fase_m(contorno=9)
print("\n")
print("m:")
print((alpha_m-m_min)/3)
alpha_c = solve_Espacio_fase_c(contorno=9)
print("\n")
print("c:")
print((alpha_c-c_min)/3)
print("\n\n")
print("Superior:\n")
alpha_m = solve_Espacio_fase_m(contorno=9,infer=1)
print("\n")
print("m:")
print((alpha_m-m_min)/3)
alpha_c = solve_Espacio_fase_c(contorno=9,infer=1)
print("\n")
print("c:")
print((alpha_c-c_min)/3)
print("\n")