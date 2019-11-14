#!/usr/bin/python3.7
#
#David Alonso Garduño Granados
#Python(3.7.4)
#14/11/19
#
def Suma(n):
    """Suma de Gauss"""
    return(n*(n+1))//2
def suma(n):
    "Suma iterativa"
    r=0
    for i in range(n+1):
	    r+=i
    return(r)
def SumaR(n):
    "Suma recursiva"
    if n==0:
	    return(0)
    else:
	    return(n+SumaR(n-1))
