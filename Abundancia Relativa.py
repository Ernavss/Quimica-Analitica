import numpy as np
import matplotlib.pyplot as plt 
from statistics import mean


#Betas de formación

b1= input ("Ingresa el valor de logB1 (si no existe, pon 0) ")
b2= input ("Ingresa el valor de logB2 (si no existe, pon 0) ")
b3= input ("Ingresa el valor de logB3 (si no existe, pon 0) ")
b4= input ("Ingresa el valor de logB4 (si no existe, pon 0) ")
B1= 10**float(b1)
B2= 10**float(b2)
B3= 10**float(b3)
B4= 10**float(b4)

#limites en x de la gráfica
x=np.array([0,12])
inf= min(x)
sup= max(x)

#phi de formación (las y representan phi)
x0=np.linspace(inf,sup,1000)
y0= (1+(B1*10**-x0)+(B2*10**-(2*x0))+(B3*10**-(3*x0))+(B4*10**-(4*x0)))**-1

x1=np.linspace(inf,sup,1000)
y1= y0*B1*10**-x0

x2=np.linspace(inf,sup,1000)
y2= y0*B2*10**-(2*x0)

x3=np.linspace(inf,sup,1000)
y3= y0*B3*10**-(3*x0)

x4=np.linspace(inf,sup,1000)
y4= y0*B4*10**-(4*x0)
#plot properties
plt.figure(figsize=(12, 8))
plt.title('Diagrama de abundancia relativa')
plt.xlabel('pL')
plt.ylabel('phi')



plt.plot(x0, y0, label="φ0")
plt.plot(x1, y1, label="φ1")
plt.plot(x2, y2, label="φ2")
plt.plot(x3, y3, label="φ3")
plt.plot(x4, y4, label="φ4")



plt.axis([0, 12, 0, 1])
plt.legend()
plt.show()


#Para determinar la composición de la mezcla: (necesitas correr el código anterior)
pL = float(input("Ingresa el valor de pL: "))
C0= float(input("Ingresa la concentración total: "))
o0= (1+(B1*10**-pL)+(B2*10**-(2*pL))+(B3*10**-(3*pL))+(B4*10**-(4*pL)))**-1
o1= o0*B1*10**-pL
o2= o0*B2*10**-(2*pL)
o3= o0*B3*10**-(3*pL)
o4= o0*B4*10**-(4*pL)
print ("[M]= ", C0*o0)
print ("[ML]= ", C0*o1)
print ("[ML2]= ", C0*o2)
print ("[ML3]= ", C0*o3)
print ("[ML4]= ", C0*o4)
