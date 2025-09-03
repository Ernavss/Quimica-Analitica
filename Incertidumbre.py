
#incertidumbre típica
import numpy as np


def promedio(data):
    prom=np.mean(data)
    print("\n \n promedio: ",prom)
    print("redondeo a ",decimales, " decimales: ", np.round(prom,decimales))
    return prom
def itipica(data,prom,Ndatos):
    i=0
    suma=0
    while i < Ndatos:
          suma=suma+(data[i]-prom)**2
          i+=1

    sx=np.sqrt(suma/(Ndatos-1))

    print("\n desviación estándar (incert. típica)", sx)
    print("redondeo a ",decimales, " decimales: ",  np.round(sx,decimales))
    return sx

#incertidumbre tipo A
def itipoA(sx,Ndatos):
    sA=sx/np.sqrt(Ndatos)

    print("\n incert. tipo A:",sA)
    print("redondeo a ",decimales, " decimales: ",np.round(sA,decimales), " cm")
    return sA

#incertidumbre combinada
def ucombinada(sA,sB):
    uc= np.sqrt(sA**2+sB**2)
    print("\n incert. combinada:",uc)
    print("redondeo a ",decimales, " decimales: ",np.round(uc,decimales), " cm")

    return uc
#Cálculo de las incertidumbres
sB= float(input("Ingresa tu incertidumbre tipo B:"))

def calculos(datos,sB, decimales):

    Ndatos=len(datos)
    prom=promedio(datos)
    sx=itipica(datos,prom,Ndatos)
    sA=itipoA(sx,Ndatos)
    uc=ucombinada(sA,sB)

    print("\n\n  Mejor estimado",": (",np.round(prom,decimales), "+/-", np.round(uc,decimales),")")
decimales=int(input("Ingresa el número de decimales que deseas:"))


inp =input("Ingresa tus datos medidos separados por un espacio: ")
l=list(map(float,inp.split()))
datos=np.array(l)
calculos(datos, sB, decimales)
