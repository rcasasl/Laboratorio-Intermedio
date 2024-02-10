import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math as m
def unpack(file_path):

    x = []
    x_title = ""
    y = []
    y_title = ""

    with open(file_path, 'r', encoding='iso-8859-1') as file:
        for line in file:
            # Process each line here
            line = line.strip()
            if line == "":
                continue
            line = line.split()
            if ord(line[0][-1]) > 57:
                x_title += line[0] + " "
                y_title += line[1] + " "
                continue
            line[0] = line[0].replace(",", ".")
            line[1] = line[1].replace(",", ".")
            x.append(float(line[0]))
            y.append(float(line[1]))
    
    return x, x_title, y, y_title

file_path = "datos1(dia1)"

x,x_title,y,y_title = unpack(file_path)

xf = []
for i in range(len(x)):
    xf.append(x[i]/(2) + 2.2)

plt.plot(xf, y)
plt.xlabel("Ángulo thetha (°)")
plt.ylabel(y_title)
xf_rad = []
for i in range(len(x)):
    xf_rad.append(x[i]*(np.pi/180)-np.pi)

xf_rad1 = [np.deg2rad(angle) for angle in x]
   
def Bragg(theta,d):
    wavelength = 2*d*np.sin(theta)
    #print(wavelength)
    return wavelength

d = 2.014*(10**(-10))

x_Bragg = Bragg(xf_rad,d)

plt.figure(figsize=(10,6))
plt.plot(x_Bragg,y)
#plt.set_title("Intensidad vs lambda, para n=1")
plt.grid(True)
plt.show()
for i in range(len(x_Bragg)):
    if y[i] == max(y):
        x_valan = x_Bragg[i]
    
print(x_valan)   

for i in range(len(xf)):
    if y[i] == max(y):
        x_val = xf[i]
    
print(x_val)   

print(x_val*(np.pi/180))
s=np.sin(x_val*(np.pi/180))
print(s)
print(2*d*s)