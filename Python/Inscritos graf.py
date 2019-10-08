#Jijón Romero Carolina 
#
#
#
#Para resolver el problema utilice las formulass de coordenadas polares a rectangulares r*senx y r*cosx
#Coordenadas de los poligonos inscritas en una circunferencia de radio r 
# Las coordenadas de los vertices de un triángulo inscrito en una circunferencia de radio r
from math import sin
from math import cos
from math import pi
from matplotlib import pyplot as plt
import numpy as np
r = 1
l = 3
a = 2*pi/l

y1=r*sin(a)
x1=r*cos(a)
y2=r*sin(2*a)
x2=r*cos(2*a)
y3=r*sin(3*a)
x3=r*cos(3*a)
print("""Las coordenadas de los vértices de un triángulo de radio r son
v1=(%g,%g)
v2=(%g,%g)
v3=(%g,%g)""" %(x1,y1,x2,y2,x3,y3))
x=np.array([x1,x2,x3,x1])
y=np.array([y1,y2,y3,y1])

circulo= plt.Circle((0,0), radius= r,color='b')
ax=plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.set_xlim([ -(r+1),(r+1) ])
ax.set_ylim([ -(r+1),(r+1) ])
plt.gca().set_aspect('equal', adjustable='box')
plt.plot(x,y , label='linear', color='r')
ax.add_patch(circulo)

plt.legend()
plt.show("Comentario de prueba")
plt.draw()

#Las coordenadas de los vértices de un cuadrado inscrito en una circunferencia de radio "r" son
r = 1
l = 4
a = 2*pi/l

xc1=r*cos(a)
yc1=r*sin(a)
xc2=r*cos(2*a)
yc2=r*sin(2*a)
xc3=r*cos(3*a)
yc3=r*sin(3*a)
xc4=r*cos(4*a)
yc4=r*sin(4*a)
print("""\nlas coordenadas de los vértices de un cuadrado inscrito en una circuferencia de radio r son
v1=(%g,%g)
v2=(%g,%g)
v3=(%g,%g)
v4=(%g,%g)""" %(xc1,yc1,xc2,yc2,xc3,yc3,xc4,yc4))
x=np.array([xc1,xc2,xc3,xc4,xc1])
y=np.array([yc1,yc2,yc3,yc4,yc1])

circulo= plt.Circle((0,0), radius= r,color='b')
ax=plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.set_xlim([ -(r+1),(r+1) ])
ax.set_ylim([ -(r+1),(r+1) ])
plt.gca().set_aspect('equal', adjustable='box')
plt.plot(x,y , label='linear', color='r')
ax.add_patch(circulo)

plt.legend()
plt.show("Comentario de prueba")
plt.draw()

#Las coordenadas de los vértices de un pentágono inscrito en una circunferencia de radio r son
r = 1
l = 5
a = 2*pi/l

xp1=r*cos(a)
yp1=r*sin(a)
xp2=r*cos(2*a)
yp2=r*sin(2*a)
xp3=r*cos(3*a)
yp3=r*sin(3*a)
xp4=r*cos(4*a)
yp4=r*sin(4*a)
xp5=r*cos(5*a)
yp5=r*sin(5*a)
print("""\nlas coordenadas de un pentágono inscrito en una circuferencia de radio r son
v1=(%g,%g)
v2=(%g,%g)
v3=(%g,%g)
v4=(%g,%g) 
v5=(%g,%g)"""%(xp1,yp1,xp2,yp2,xp3,yp3,xp4,yp4,xp5,yp5))
x=np.array([xp1,xp2,xp3,xp4,xp5,xp1])
y=np.array([yp1,yp2,yp3,yp4,yp5,yp1])

circulo= plt.Circle((0,0), radius= r,color='b')
ax=plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.set_xlim([ -(r+1),(r+1) ])
ax.set_ylim([ -(r+1),(r+1) ])
plt.gca().set_aspect('equal', adjustable='box')
plt.plot(x,y , label='linear', color='r')
ax.add_patch(circulo)

plt.legend()
plt.show("Comentario de prueba")
plt.draw()

#Las coordenadas de los vértices de un hexágono inscrito en una circuferencia de radio r son
r = 1
l = 6
a = 2*pi/l

xh1=r*cos(a)
yh1=r*sin(a)
xh2=r*cos(2*a)
yh2=r*sin(2*a)
xh3=r*cos(3*a)
yh3=r*sin(3*a)
xh4=r*cos(4*a)
yh4=r*sin(4*a)
xh5=r*cos(5*a)
yh5=r*sin(5*a)
xh6=r*cos(6*a)
yh6=r*sin(6*a)
print("""\nlas coordenadas de un hexágono inscrito en una circunferencia de radio r son
v1=(%g,%g)
v2=(%g,%g)
v3=(%g,%g)
v4=(%g,%g)
v5=(%g,%g)
v6=(%g,%g)"""%(xh1,yh1,xh2,yh2,xh3,yh3,xh4,yh4,xh5,yh5,xh6,yh6))
x=np.array([xh1,xh2,xh3,xh4,xh5,xh6,xh1])
y=np.array([yh1,yh2,yh3,yh4,yh5,yh6,yh1])

circulo= plt.Circle((0,0), radius= r,color='b')
ax=plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.set_xlim([ -(r+1),(r+1) ])
ax.set_ylim([ -(r+1),(r+1) ])
plt.gca().set_aspect('equal', adjustable='box')
plt.plot(x,y , label='linear', color='r')
ax.add_patch(circulo)

plt.legend()
plt.show("Comentario de prueba")
plt.draw()

#Las coordenadas de los vértices de un heptágono inscrito en una circunferencia de radio r son
r = 1
l = 7
a = 2*pi/l

xe1=r*cos(a)
ye1=r*sin(a)
xe2=r*cos(a*2)
ye2=r*sin(2*a)
xe3=r*cos(3*a)
ye3=r*sin(3*a)
xe4=r*cos(4*a)
ye4=r*sin(4*a)
xe5=r*cos(5*a)
ye5=r*sin(5*a)
xe6=r*cos(6*a)
ye6=r*sin(6*a)
xe7=r*cos(7*a)
ye7=r*sin(7*a)
print("""\nlas coordenadas de un heptágono inscrito en una circunferencia de radio r son:
v1=(%g,%g)
v2=(%g,%g)
v3=(%g,%g)
v4=(%g,%g)
v5=(%g,%g)
v6=(%g,%g)
v7=(%g,%g)"""%(xe1,ye1,xe2,ye2,xe3,ye3,xe4,ye4,xe5,ye5,xe6,ye6,xe7,ye7))
x=np.array([xe1,xe2,xe3,xe4,xe5,xe6,xe7,xe1])
y=np.array([ye1,ye2,ye3,ye4,ye5,ye6,ye7,ye1])

circulo= plt.Circle((0,0), radius= r,color='b')
ax=plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.set_xlim([ -(r+1),(r+1) ])
ax.set_ylim([ -(r+1),(r+1) ])
plt.gca().set_aspect('equal', adjustable='box')
plt.plot(x,y , label='linear', color='r')
ax.add_patch(circulo)

plt.legend()
plt.show("Comentario de prueba")
plt.draw()

#Las coordenadas de un octagono inscrito en una circunferencia de radio r son :
r = 1
l = 8
a = 2*pi/l

xo1=r*cos(a)
yo1=r*sin(a)
xo2=r*cos(2*a)
yo2=r*sin(2*a)
xo3=r*cos(3*a)
yo3=r*sin(3*a)
xo4=r*cos(4*a)
yo4=r*sin(4*a)
xo5=r*cos(5*a)
yo5=r*sin(5*a)
xo6=r*cos(6*a)
yo6=r*sin(6*a)
xo7=r*cos(7*a)
yo7=r*sin(7*a)
xo8=r*cos(8*a)
yo8=r*sin(8*a)
print("""\nlas coordenadas de un octágono inscrito en una circunferencia de radio r son:
v1=(%g,%g)
v2=(%g,%g)
v3=(%g,%g)
v4=(%g,%g)
v5=(%g,%g)
v6=(%g,%g)
v7=(%g,%g)
v8=(%g,%g)"""%(xo1,yo1,xo2,yo2,xo3,yo3,xo4,yo4,xo5,yo5,xo6,yo6,xo7,yo7,xo8,xo8))
x=np.array([xo1,xo2,xo3,xo4,xo5,xo6,xo7,xo8,xo1])
y=np.array([yo1,yo2,yo3,yo4,yo5,yo6,yo7,yo8,yo1])

circulo= plt.Circle((0,0), radius= r,color='b')
ax=plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.set_xlim([ -(r+1),(r+1) ])
ax.set_ylim([ -(r+1),(r+1) ])
plt.gca().set_aspect('equal', adjustable='box')
plt.plot(x,y , label='linear', color='r')
ax.add_patch(circulo)

plt.legend()
plt.show("Comentario de prueba")
plt.draw()



#Las coordenadas de un eneagono inscrito en una circunferencia de radio r son :
r = 1
l = 9
a = 2*pi/l

xg1=r*cos(a)
yg1=r*sin(a)
xg2=r*cos(2*a)
yg2=r*sin(2*a)
xg3=r*cos(3*a)
yg3=r*sin(3*a)
xg4=r*cos(4*a)
yg4=r*sin(4*a)
xg5=r*cos(5*a)
yg5=r*sin(5*a)
xg6=r*cos(6*a)
yg6=r*sin(6*a)
xg7=r*cos(7*a)
yg7=r*sin(7*a)
xg8=r*cos(8*a)
yg8=r*sin(8*a)
xg9=r*cos(9*a)
yg9=r*sin(9*a)
print("""Las coordenadas de los vértices de un eneágono inscrito en una circunferencia son:
v1=(%g,%g)
v2=(%g,%g)
v3=(%g,%g)
v4=(%g,%g)
v5=(%g,%g)
v6=(%g,%g)
v7=(%g,%g)
v8=(%g,%g)
v9=(%g,%g)"""%(xg1,yg1,xg2,yg2,xg3,yg3,xg4,yg4,xg5,yg5,xg6,yg6,xg7,yg7,xg8,yg8,xg9,yg9))
x=np.array([xg1,xg2,xg3,xg4,xg5,xg6,xg7,xg8,xg9,xg1])
y=np.array([yg1,yg2,yg3,yg4,yg5,yg6,yg7,yg8,yg9,yg1])

circulo= plt.Circle((0,0), radius= r,color='b')
ax=plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.set_xlim([ -(r+1),(r+1) ])
ax.set_ylim([ -(r+1),(r+1) ])
plt.gca().set_aspect('equal', adjustable='box')
plt.plot(x,y , label='linear', color='r')
ax.add_patch(circulo)

plt.legend()
plt.show("Comentario de prueba")
plt.draw()


#Las coordenadas de un decagono inscrito en una circunferencia de radio r son :
r = 1
l = 10
a = 2*pi/l

xd1=r*cos(a)
yd1=r*sin(a)
xd2=r*cos(2*a)
yd2=r*sin(2*a)
xd3=r*cos(3*a)
yd3=r*sin(3*a)
xd4=r*cos(4*a)
yd4=r*sin(4*a)
xd5=r*cos(5*a)
yd5=r*sin(5*a)
xd6=r*cos(6*a)
yd6=r*sin(6*a)
xd7=r*cos(7*a)
yd7=r*sin(7*a)
xd8=r*cos(8*a)
yd8=r*sin(8*a)
xd9=r*cos(9*a)
yd9=r*sin(9*a)
xd10=r*cos(10*a)
yd10=r*sin(10*a)
print("""Las coordenadas de los vértices de un decágono inscrito en una circunferencia son:
v1=(%g,%g)
v2=(%g,%g)
v3=(%g,%g)
v4=(%g,%g)
v5=(%g,%g)
v6=(%g,%g)
v7=(%g,%g)
v8=(%g,%g)
v9=(%g,%g)
v10=(%g,%g)"""%(xd1,yd1,xd2,yd2,xd3,yd3,xd4,yd4,xd5,yd5,xd6,yd6,xd7,yd7,xd8,yd8,xd9,yd9,xd10,yd10))
x=np.array([xd1,xd2,xd3,xd4,xd5,xd6,xd7,xd8,xd9,xd10,xd1])
y=np.array([yd1,yd2,yd3,yd4,yd5,yd6,yd7,yd8,yd9,yd10,yd1])

circulo= plt.Circle((0,0), radius= r,color='b')
ax=plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.set_xlim([ -(r+1),(r+1) ])
ax.set_ylim([ -(r+1),(r+1) ])
plt.gca().set_aspect('equal', adjustable='box')
plt.plot(x,y , label='linear', color='r')
ax.add_patch(circulo)

plt.legend()
plt.show("Comentario de prueba")
plt.draw()

#Las coordenadas de un decagono inscrito en una circunferencia de radio r son :
r = 1
l = 11
a = 2*pi/l

xt1=r*cos(a)
yt1=r*sin(a)
xt2=r*cos(2*a)
yt2=r*sin(2*a)
xt3=r*cos(3*a)
yt3=r*sin(3*a)
xt4=r*cos(4*a)
yt4=r*sin(4*a)
xt5=r*cos(5*a)
yt5=r*sin(5*a)
xt6=r*cos(6*a)
yt6=r*sin(6*a)
xt7=r*cos(7*a)
yt7=r*sin(7*a)
xt8=r*cos(8*a)
yt8=r*sin(8*a)
xt9=r*cos(9*a)
yt9=r*sin(9*a)
xt10=r*cos(10*a)
yt10=r*sin(10*a)
xt11=r*cos(11*a)
yt11=r*sin(11*a)

print("""Las coordenadas de los vértices de un decágono inscrito en una circunferencia son:
v1=(%g,%g)
v2=(%g,%g)
v3=(%g,%g)
v4=(%g,%g)
v5=(%g,%g)
v6=(%g,%g)
v7=(%g,%g)
v8=(%g,%g)
v9=(%g,%g)
v10=(%g,%g)
v11=(%g,%g)"""%(xt1,yt1,xt2,yt2,xt3,yt3,xt4,yt4,xt5,yt5,xt6,yt6,xt7,yt7,xt8,yt8,xt9,yt9,xt10,yt10,xt11,yt11))
x=np.array([xt1,xt2,xt3,xt4,xt5,xt6,xt7,xt8,xt9,xt10,xt11,xt1])
y=np.array([yt1,yt2,yt3,yt4,yt5,yt6,yt7,yt8,yt9,yt10,yt11,yt1])

circulo= plt.Circle((0,0), radius= r,color='b')
ax=plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.set_xlim([ -(r+1),(r+1) ])
ax.set_ylim([ -(r+1),(r+1) ])
plt.gca().set_aspect('equal', adjustable='box')
plt.plot(x,y , label='linear', color='r')
ax.add_patch(circulo)

plt.legend()
plt.show("Comentario de prueba")
plt.draw()

#Las coordenadas de un decagono inscrito en una circunferencia de radio r son :
r = 1
l = 12
a = 2*pi/l

xm1=r*cos(a)
ym1=r*sin(a)
xm2=r*cos(2*a)
ym2=r*sin(2*a)
xm3=r*cos(3*a)
ym3=r*sin(3*a)
xm4=r*cos(4*a)
ym4=r*sin(4*a)
xm5=r*cos(5*a)
ym5=r*sin(5*a)
xm6=r*cos(6*a)
ym6=r*sin(6*a)
xm7=r*cos(7*a)
ym7=r*sin(7*a)
xm8=r*cos(8*a)
ym8=r*sin(8*a)
xm9=r*cos(9*a)
ym9=r*sin(9*a)
xm10=r*cos(10*a)
ym10=r*sin(10*a)
xm11=r*cos(11*a)
ym11=r*sin(11*a)
xm12=r*cos(12*a)
ym12=r*sin(12*a)
print("""Las coordenadas de los vértices de un decágono inscrito en una circunferencia son:
v1=(%g,%g)
v2=(%g,%g)
v3=(%g,%g)
v4=(%g,%g)
v5=(%g,%g)
v6=(%g,%g)
v7=(%g,%g)
v8=(%g,%g)
v9=(%g,%g)
v10=(%g,%g)
v11=(%g,%g)
v12=(%g,%g)"""%(xm1,ym1,xm2,ym2,xm3,ym3,xm4,ym4,xm5,ym5,xm6,ym6,xm7,ym7,xm8,ym8,xm9,ym9,xm10,ym10,xm11,ym11,xm12,ym12))
x=np.array([xm1,xm2,xm3,xm4,xm5,xm6,xm7,xm8,xm9,xm10,xm11,xm12,xm1])
y=np.array([ym1,ym2,ym3,ym4,ym5,ym6,ym7,ym8,ym9,ym10,ym11,ym12,ym1])

circulo= plt.Circle((0,0), radius= r,color='b')
ax=plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.set_xlim([ -(r+1),(r+1) ])
ax.set_ylim([ -(r+1),(r+1) ])
plt.gca().set_aspect('equal', adjustable='box')
plt.plot(x,y , label='linear', color='r')
ax.add_patch(circulo)

plt.legend()
plt.show("Comentario de prueba")
plt.draw()

