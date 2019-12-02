#!/usr/bin/python3.7
#
#David Alonso Garduño Granados
#Python(3.7.4)
#David Alonso Garduño Granados
#01/12/19
#01/12/19
#Evaluación práctica
"""Definimos la base del rectángulo de base "b"(depende de cada número)
y el lado = 1)"""
bases=[]
alturas=[]
b=81
x=b
h=1
print("________________________________________________")
print("La raíz cuadrada de %g puede ser encontrada con:"%(b))
print("|rectangulo   |   base    |   altura   |")
print("|      1      |   %5.4f   |   %5.4f    |"%(b,h))
for i in range(2,8):
    b=(b+h)/2
    h=x/b
    bases.append(b)
    alturas.append(h)
    print("|      %g      |   %5.4f   |   %5.4f    |"%(i,b,h))
"""Repetimos este proceso con cada uno de las raices a encontrar"""

bases=[]
alturas=[]
b=95
x=b
h=1
print("________________________________________________")
print("La raíz cuadrada de %g puede ser encontrada con:"%(b))
print("|rectangulo   |   base    |   altura   |")
print("|      1      |   %5.4f   |   %5.4f    |"%(b,h))
for i in range(2,8):
    b=(b+h)/2
    h=x/b
    bases.append(b)
    alturas.append(h)
    print("|      %g      |   %5.4f   |   %5.4f    |"%(i,b,h))

bases=[]
alturas=[]
b=0.5
x=b
h=1
print("________________________________________________")
print("La raíz cuadrada de %g puede ser encontrada con:"%(b))
print("|rectangulo   |   base    |   altura   |")
print("|      1      |   %5.4f   |   %5.4f    |"%(b,h))
for i in range(2,5):
    b=(b+h)/2
    h=x/b
    bases.append(b)
    alturas.append(h)
    print("|      %g      |   %5.4f   |   %5.4f    |"%(i,b,h))

bases=[]
alturas=[]
b=0.125
x=b
h=1
print("________________________________________________")
print("La raíz cuadrada de %g puede ser encontrada con:"%(b))
print("|rectangulo   |   base    |   altura   |")
print("|      1      |   %5.4f   |   %5.4f    |"%(b,h))
for i in range(2,7):
    b=(b+h)/2
    h=x/b
    bases.append(b)
    alturas.append(h)
    print("|      %g      |   %5.4f   |   %5.4f    |"%(i,b,h))
