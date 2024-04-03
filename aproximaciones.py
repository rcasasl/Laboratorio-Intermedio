import numpy as np
import matplotlib.pyplot as plt

v = np.array([0.98,1.98,2.98,3.97,4.95,5.95,6.93,7.93,8.91])
u = np.array([(i*10) for i in range(1,10)])

plt.scatter(u,v)
plt.title('Corriente (uA) vs Voltaje (mV)')
plt.xlabel('Corriente (uA)')
plt.ylabel('Voltaje (mV)')
plt.show()

def aproximacion_c_m(u,v):
    a = u**2
    b = v
    c = u
    d = b*c

    C = (np.sum(a)*np.sum(b) - np.sum(c)*np.sum(d))/(len(u)*np.sum(a) - np.sum(c)**2)
    M = (len(u)*np.sum(d) - np.sum(c)*np.sum(b))/(len(u)*np.sum(a) - np.sum(c)**2)

    aCU = np.sqrt((1/(len(u)-2))*np.sum((b - C - M*c)**2))

    aC = aCU*np.sqrt(np.sum(a)/(len(u)*np.sum(a) - np.sum(c)**2))
    aM = aCU*np.sqrt(len(u)/(len(u)*np.sum(a) - np.sum(c)**2))

    return C, M, aC, aM, aCU

C,M,aC,aM,aCU = aproximacion_c_m(u,v)

X = u
Y = M*X + C

print(C,M,aC,aM,aCU)

plt.title('Linealización Corriente (uA) vs Voltaje (mV)')
plt.xlabel('Corriente ln(uA)')
plt.ylabel('Voltaje ln(mV)')
plt.scatter(X,v)
plt.plot(X,Y)
plt.show()

plt.title('Residuos Linealización Corriente (uA) vs Voltaje (mV)')
plt.xlabel('Corriente ln(uA)')
plt.ylabel('Voltaje ln(mV) Medida - Voltaje ln(mV) del modelo')
plt.scatter(X,v - Y)
plt.show()