#!/usr/bin/python3.7
#
#David Alonso Garduño Granados
#Python(3.7.4)
#01/12/19
#01/12/19
#Se reparte la soda
def soda(n):
    A=n//3
    B=1000-n-A
    return(B)
n=int(input())
print(soda(n))
