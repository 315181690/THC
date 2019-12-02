#!/usr/bin/python3.7
#
#David Alonso Garduño Granados
#Python(3.7.4)
#01/12/19
#01/12/19
#Mis funciones.py con ellas trabajamos en muchas clases
"""
Funciones definidas por el usuario
"""
def vabs(x):
    '''Regresa el valor absoluto del numero x.
Regresa  x si x es mayor que cero
Regresa -x si x es menor que cero
'''
    if x>=0:
        x=x
    else:
        x=-1*x
    return(x)

def signo(x):
    '''Regresa el signo del numero x.
Regresa  1 si x es positivo
Regresa  0 si x es cero
Regresa -1 si x es negativo
'''
    if x>0:
        x=1
    else:
        if x<0:
            x=-1
        else:
            x=0
    return(x)

def multiplica(a,b):
    '''Regresa el resultado de multiplicar
    el numero a por el numero b
'''
    x=a*b
    return(x)

def elMayor(a,b):
    '''Regresa el mayor de los numeros: a, b
'''
    if a>b:
        x=a
    else:
        x=b
    return(x)

def elMenor(a,b):
    '''Regresa el menor de los numeros: a, b
'''
    if a<b:
        x=a
    else:
        x=b
    return(x)

def rectangular(x):
    '''Regresa la evaluacion de x en
la funcion definida como:
Regresa 0   si |x| > 1/2
Regresa 1/2 si |x| = 1/2
Regresa 1   si |x| < 1/2
'''
    if vabs(x)<1/2:
        x=1
    else:
        if vabs(x)>1/2:
            x=0
        else:
            x=1/2
    return(x)

def identidad(x):
    '''regresa la identidad del valor x
'''
    x=x
    return(x)

def rampa(x):
    '''Regresa 0 si x < 0
Regresa x si x >= 0
'''
    if x<0:
        x=0
    else:
        x=x
    return(x)

def parte_entera(x):
    ''' Regresa la parte entera de x,
por ejemplo si x = 9.23 regresa 9
'''
    x=x//1
    return(x)

def enteroMayor(x):
    '''Regresa el entero mayor de x
ej, si x = 7.1 regresaria 8
'''
    x=x//1+1
    return(x)

def enteroMenor(x):
    '''Regresa el entero meno de x
ej, si x = 7.1 regresaria 7
'''
    x=x//1
    return(x)

def parte_fraccionaria(x):
    ''' Regresa la parte fraccionaria de x definida como
x - enteroMenor(x)
ej, si x = 9.23 regresaria:
    9.23 - floor(9.23) = 9.23 - 9
regresa 0.23
ej, si x = -7.26 regresaria:
    -7.26 - floor(-7.26) = -7.26 - (-8) = -7.26 + 8
regresa 0.74
'''
    from math import floor
    x=x-floor(x)
    return(x)

def ulam(n):
    '''Regresa n/2 si n es par
Regresa 3*n + 1 si n es impar
'''
    if n/2==floor(n/2):
        x=n/2
    else:
        x=3*n+1
    return(x)
