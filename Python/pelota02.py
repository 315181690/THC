#!/usr/bin/python3.7
#
#David Alonso Garduño Granados
#Python(3.7.4)
#01/12/19
#01/12/19
# Calcula la posición de una pelota con una velocidad inicial
# de 5 m/s y un tiempo de 0.6 segundos
v0 = 5
g = 9.81
t = 0.6
y = v0*t - .5*g*t**2
print(y)
