#!/usr/bin/python3.7
#
#David Alonso Garduño Granados
#Python(3.7.4)
#01/12/19
#01/12/19
#Un ejemplo con comentarios de como funciona el modulo matplot
from math import sin, cos, sqrt, pi

import matplotlib.pyplot as plt
import numpy as np

r = 5
l = 5
a = 2*pi/l


x1 = r*cos(a)
x2 = r*cos(2*a)
x3 = r*cos(3*a)
x4 = r*cos(4*a)
x5 = r*cos(5*a)

y1 = r*sin(a)
y2 = r*sin(2*a)
y3 = r*sin(3*a)
y4 = r*sin(4*a)
y5 = r*sin(5*a)

x = np.array([x1,x2,x3,x4,x5,x1]) # Asigna a x el valor de la lisya definida en entre los corchetes
y = np.array([y1,y2,y3,y4,y5,y1])


print("""Las coordenadas del pentagono
inscrito en una circunferencia de radio %f
son:
A = (%5.2f,%5.2f)
B = (%5.2f,%5.2f)
C = (%5.2f,%5.2f)
D = (%5.2f,%5.2f)
E = (%5.2f,%5.2f)
"""%(r, x1, y2, x2, y2, x3, y3 ,x4 ,y4 ,x5 ,y5))

circulo = plt.Circle((0,0), radius=r, color='b') #Estamos definiendo las características del círculo
ax=plt.gca() #definimos los ejes
ax.spines['left'].set_position('center') #Centramos el eje horizontal
ax.spines['bottom'].set_position('center') #Centramos el eje vertical

plt.gca().set_aspect('equal', adjustable='box') #definimos que la apriencia sea simétrica
plt.plot(x, y, label='linear', color='r') #Los valores guardados en x y y se piden mostrar y establecemos las características de los mismos
ax.add_patch(circulo) #añadimos el circulo



plt.legend() #muestra la etiqueta como una leyenda
#plt.show() # 
plt.draw() #Sobrepone las figuras

l = 3
a = 2*pi/l
R = pi

x1 = 5*cos(R + a)
x2 = 5*cos(R + 2*a)
x3 = 5*cos(R + 3*a)

y1 = 5*sin(R + a)
y2 = 5*sin(R + 2*a)
y3 = 5*sin(R + 3*a)

x = np.array([x1,x2,x3,x1])
y = np.array([y1,y2,y3,y1])

circulo= plt.Circle((0,0), radius= 5,color='b')
ax=plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.set_xlim([ -(r+1),(r+1) ])
ax.set_ylim([ -(r+1),(r+1) ])
plt.gca().set_aspect('equal', adjustable='box')
plt.plot(x, y, label='linear', color='r')
ax.add_patch(circulo)

plt.legend()
plt.show()
