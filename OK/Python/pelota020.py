#!/usr/bin/python3.7
#
#David Alonso Garduño Granados
#Python(3.7.4)
#01/12/19
#01/12/19
#Calcula la posición de una pelota con una velocidad inicial
# de 5 m/s y un tiempo de 0.6 segundos
v0 = 5
g = 9.81
t = 0.6
y = v0*t - .5*g*t**2

print(y)
print('En el tiempo t=%g segundos, la altura de la pelota es %.2f metros'%(t,y))
print("""
En t=%g segundos, la pelota con
velocidad inicial v0=%.3E m/s
se encuentra a %.2 metros de altura."""%(t,v0,y))
print("En t=%g segundos, la pelota con\nvelocidad inicial v0=%.3E m/s\nse encuentra a %.2 metros de altura."%(t,v0,y))
"""
este es un comentario
multilinea
"""
