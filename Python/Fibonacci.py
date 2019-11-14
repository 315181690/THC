#!/usr/bin/python3.7
#
#David Alonso Garduño Granados
#Python(3.7.4)
#14/11/19
#
def Fib(n):
    if 0<=n<2:
	    return(1)
    else:
	    return(Fib(n-1)+Fib(n-2))
