#!/usr/bin/python3.7
#
#David Alonso Garduño Granados
#Python(3.7.4)
#01/12/19
#01/12/19
#Definimos la sucesión de fibonacci de manera recursiva
def Fib(n):
    if 0<=n<2:
	    return(1)
    else:
	    return(Fib(n-1)+Fib(n-2))
