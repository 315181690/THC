#!/usr/bin/python3.7
#
#David Alonso Garduño Granados
#Python(3.7.4)
#01/12/19
#01/12/19
#Resuelve el problema de el fractal de cantor
def dividir(a,b):
    c = a + 1/3*(b-a)
    d = a + 2/3*(b-a)
    return([[a,c],[d,b]])

nl = []
ne = dividir(0,1)

"""for elemento in ne:
    [r1,r2]=dividir(elemento[0],elemento[1])
    nl.append(r1)
    nl.append(r2)
print(nl)"""
for i in range(5):
    nl=[]
    for elemento in ne:
        [r1,r2]=dividir(elemento[0],elemento[1])
        nl.append(r1)
        nl.append(r2)
    ne=nl.copy()
print(nl)
