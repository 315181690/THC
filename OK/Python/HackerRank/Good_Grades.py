#!/usr/bin/python3.7
#
#David Alonso Garduño Granados
#Python(3.7.4)
#01/12/19
#01/12/19
#Dependiendo de la calificación se asigna una letra 
def GG(n):
    if 0<=n<=59:
        return('F')
    if 60<=n<=69:
        return('D')
    if 70<=n<=79:
        return('C')
    if 80<=n<=89:
        return('B')
    if 90<=n<=100:
        return('A')
n=int(input())
print(GG(n))
