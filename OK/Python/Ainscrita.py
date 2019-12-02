#!/usr/bin/python3.7
#
#David Alonso Garduño Granados
#Python(3.7.4)
#Area de figuras inscritas en una circunferencia
#01/12/19
#01/12/19
from math import sin, cos, pi, sqrt
import matplotlib.pyplot as plt
import numpy as np
def ains(n,r):
    """Definir el número de lados del poligono.
Y el radio de la circunferencia inscrita."""
    if n>=5:
        an=(2*pi/n)/2
        h=r*cos(an)
        l=sqrt(-h**2+r**2)*2
        a=(n*l*h)/2
        return(a)
#Calcula el area de figuras inscritas en una circunferencia
