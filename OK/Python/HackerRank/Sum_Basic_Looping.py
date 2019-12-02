#!/usr/bin/python3.7
#
#David Alonso Garduño Granados
#Python(3.7.4)
#01/12/19
#01/12/19
#Se realiza la suma de n terminos de manera recursiva
def Sloop(x):
    if x==1:
        return(1)
    else:
        return(x+Sloop(x-1))
n=int(input())
print(Sloop(n))
