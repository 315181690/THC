#David Alonso Garduño Granados
#
#
#
from math import sin, cos, pi
import matplotlib.pyplot as plt
import numpy as np

#Para el ejercicio pasaremos de coordenadas polares a escalares usando las siguientes fórmulas: y=rsinA y x=rcosA
#Los vértices de un triángulo inscrito en una circunferencia de radio r están definidos por las coordenadas polares de la misma
"definimos r como 1"
r=1
lt=3
a=2*pi/lt

y1=r*sin(a)
x1=r*cos(a)
y2=r*sin(2*a)
x2=r*cos(2*a)
y3=r*sin(3*a)
x3=r*cos(3*a)

x=np.array([x1,x2,x3,x1])
y=np.array([y1,y2,y3,y1])

print("Las coordenadas de los vértices de un triángulo de radio r son:\n v1=(%5.2f,%5.2f)\n v2=(%5.2f,%5.2f)\n v3=(%5.2f,%5.2f)" %(x1,y1,x2,y2,x3,y3))

circulo= plt.Circle((0,0), radius= r,color='b')
ax=plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.set_xlim([ -(r+1),(r+1) ])
ax.set_ylim([ -(r+1),(r+1) ])
plt.gca().set_aspect('equal', adjustable='box')
plt.plot(x, y, label='linear', color='r')
ax.add_patch(circulo)

plt.legend()
plt.show("Comentario de prueba")
plt.draw()

#Los vértices de un cuadrado inscrito en una circunferencia de radio "r" son

lc=4
ac=2*pi/lc

xc1=r*cos(ac)
yc1=r*sin(ac)
xc2=r*cos(2*ac)
yc2=r*sin(2*ac)
xc3=r*cos(3*ac)
yc3=r*sin(3*ac)
xc4=r*cos(4*ac)
yc4=r*sin(4*ac)

xc = np.array([xc1,xc2,xc3,xc4,xc1])
yc = np.array([yc1,yc2,yc3,yc4,yc1])

print("\nlas coordenadas de los vértices de un cuadrado inscrito en una circuferencia de radio r son:\n v1=(%5.2f,%5.2f)\n v2=(%5.2f,%5.2f)\n v3=(%5.2f,%5.2f)\n v4=(%5.2f,%5.2f)"%(xc1,yc1,xc2,yc2,xc3,yc3,xc4,yc4))

circulo = plt.Circle((0,0), radius=r, color='b')
ax=plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

plt.gca().set_aspect('equal', adjustable='box')
plt.plot(xc, yc, label='linear', color='r')
ax.add_patch(circulo)

plt.legend()
plt.show("Comentario de prueba")
plt.draw()

#los vértices de un pentágono inscrito en una circunferencia de radio r son

lp=5
ap=2*pi/lp

xp1=r*cos(ap)
yp1=r*sin(ap)
xp2=r*cos(2*ap)
yp2=r*sin(2*ap)
xp3=r*cos(3*ap)
yp3=r*sin(3*ap)
xp4=r*cos(4*ap)
yp4=r*sin(4*ap)
xp5=r*cos(5*ap)
yp5=r*sin(5*ap)

xp=np.array([xp1,xp2,xp3,xp4,xp5,xp1])
yp=np.array([yp1,yp2,yp3,yp4,yp5,yp1])

print("\nlas coordenadas de un pentágono inscrito en una circuferencia de radio r son:\n v1=(%5.2f,%5.2f)\n v2=(%5.2f,%5.2f)\n v3=(%5.2f,%5.2f)\n v4=(%5.2f,%5.2f)\n v5=(%5.2f,%5.2f)"%(xp1,yp1,xp2,yp2,xp3,yp3,xp4,yp4,xp5,yp5))

circulo = plt.Circle((0,0), radius=r, color='b')
ax=plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

plt.gca().set_aspect('equal', adjustable='box')
plt.plot(xp, yp, label='linear', color='r')
ax.add_patch(circulo)

plt.legend()
plt.show()
plt.draw() 

#los vértices de un hexágono inscrito en una circuferencia de radio r son

lh=6
ah=2*pi/lh

xh1=r*cos(ah)
yh1=r*sin(ah)
xh2=r*cos(2*ah)
yh2=r*sin(2*ah)
xh3=r*cos(3*ah)
yh3=r*sin(3*ah)
xh4=r*cos(4*ah)
yh4=r*sin(4*ah)
xh5=r*cos(5*ah)
yh5=r*sin(5*ah)
xh6=r*cos(6*ah)
yh6=r*sin(6*ah)

xh=np.array([xh1,xh2,xh3,xh4,xh5,xh6,xh1])
yh=np.array([yh1,yh2,yh3,yh4,yh5,yh6,yh1])

print("\nlas coordenadas de un hexágono inscrito en una circunferencia de radio r son:\n v1=(%5.2f,%5.2f)\n v2=(%5.2f,%5.2f)\n v3=(%5.2f,%5.2f)\n v4=(%5.2f,%5.2f)\n v5=(%5.2f,%5.2f)\n v6=(%5.2f,%5.2f)"%(xh1,yh1,xh2,yh2,xh3,yh3,xh4,yh4,xh5,yh5,xh6,yh6))

circulo = plt.Circle((0,0), radius=r, color='b')
ax=plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

plt.gca().set_aspect('equal', adjustable='box')
plt.plot(xh, yh, label='linear', color='r')
ax.add_patch(circulo)

plt.legend()
plt.show()
#plt.draw() 

#los vértices de un heptágono inscrito en una circunferencia de radio r son

le=7
ae=2*pi/le

xe1=r*cos(ae)
ye1=r*sin(ae)
xe2=r*cos(2*ae)
ye2=r*sin(2*ae)
xe3=r*cos(3*ae)
ye3=r*sin(3*ae)
xe4=r*cos(4*ae)
ye4=r*sin(4*ae)
xe5=r*cos(5*ae)
ye5=r*sin(5*ae)
xe6=r*cos(6*ae)
ye6=r*sin(6*ae)
xe7=r*cos(7*ae)
ye7=r*sin(7*ae)

xe=np.array([xe1,xe2,xe3,xe4,xe5,xe6,ye7,xe1])
ye=np.array([ye1,ye2,ye3,ye4,ye5,ye6,ye7,ye1])

print("\nlas coordenadas de los vértices de un heptágono inscrito en una circunferencia de radio r son:\n v1=(%5.2f,%5.2f)\n v2=(%5.2f,%5.2f)\n v3=(%5.2f,%5.2f)\n v4=(%5.2f,%5.2f)\n v5=(%5.2f,%5.2f)\n v6=(%5.2f,%5.2f)\n v7=(%5.2f,%5.2f)"%(xe1,ye1,xe2,ye2,xe3,ye3,xe4,ye4,xe5,ye5,xe6,ye6,xe7,ye7))

circulo = plt.Circle((0,0), radius=r, color='b')
ax=plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

plt.gca().set_aspect('equal', adjustable='box')
plt.plot(xe, ye, label='linear', color='r')
ax.add_patch(circulo)

plt.legend()
plt.show() 
plt.draw() 

#Los vértices de un otcágono inscrito en una circunferencia de radio r son

lo=8
ao=2*pi/lo

xo1=r*cos(ao)
yo1=r*sin(ao)
xo2=r*cos(2*ao)
yo2=r*sin(2*ao)
xo3=r*cos(3*ao)
yo3=r*sin(3*ao)
xo4=r*cos(4*ao)
yo4=r*sin(4*ao)
xo5=r*cos(5*ao)
yo5=r*sin(5*ao)
xo6=r*cos(6*ao)
yo6=r*sin(6*ao)
xo7=r*cos(7*ao)
yo7=r*sin(7*ao)
xo8=r*cos(8*ao)
yo8=r*sin(8*ao)

xo=np.array([xo1,xo2,xo3,xo4,xo5,xo6,yo7,xo8,xo1])
yo=np.array([yo1,yo2,yo3,yo4,yo5,yo6,yo7,yo8,yo1])

print("""Las coordenadas de los vértices de un octágono inscrito en una circunferencia son:
v1=(%5.2f,%5.2f)
v2=(%5.2f,%5.2f)
v3=(%5.2f,%5.2f)
v4=(%5.2f,%5.2f)
v5=(%5.2f,%5.2f)
v6=(%5.2f,%5.2f)
v7=(%5.2f,%5.2f)
v8=(%5.2f,%5.2f)"""%(xo1,yo1,xo2,yo2,xo3,yo3,xo4,yo4,xo5,yo5,xo6,yo6,xo7,yo7,xo8,yo8))

circulo = plt.Circle((0,0), radius=r, color='b')
ax=plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

plt.gca().set_aspect('equal', adjustable='box')
plt.plot(xo, yo, label='linear', color='r')
ax.add_patch(circulo)

plt.legend()
plt.show()
plt.draw()

#Los vértices de un eneágono inscrito en una circunferencia son:
n=9
ng=2*pi/n

xa1=r*cos(ng)
ya1=r*sin(ng)
xa2=r*cos(2*ng)
ya2=r*sin(2*ng)
xa3=r*cos(3*ng)
ya3=r*sin(3*ng)
xa4=r*cos(4*ng)
ya4=r*sin(4*ng)
xa5=r*cos(5*ng)
ya5=r*sin(5*ng)
xa6=r*cos(6*ng)
ya6=r*sin(6*ng)
xa7=r*cos(7*ng)
ya7=r*sin(7*ng)
xa8=r*cos(8*ng)
ya8=r*sin(8*ng)
xa9=r*cos(9*ng)
ya9=r*sin(9*ng)

xa=np.array([xa1,xa2,xa3,xa4,xa5,xa6,ya7,xa8,xa9,xa1])
ya=np.array([ya1,ya2,ya3,ya4,ya5,ya6,ya7,ya8,ya9,ya1])

print("""Las coordenadas de los vértices de un eneágono inscrito en una circunferencia son:
v1=(%5.2f,%5.2f)
v2=(%5.2f,%5.2f)
v3=(%5.2f,%5.2f)
v4=(%5.2f,%5.2f)
v5=(%5.2f,%5.2f)
v6=(%5.2f,%5.2f)
v7=(%5.2f,%5.2f)
v8=(%5.2f,%5.2f)
v9=(%5.2f,%5.2f)"""%(xa1,ya1,xa2,ya2,xa3,ya3,xa4,ya4,xa5,ya5,xa6,ya6,xa7,ya7,xa8,ya8,xa9,ya9))

circulo = plt.Circle((0,0), radius=r, color='b')
ax=plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

plt.gca().set_aspect('equal', adjustable='box')
plt.plot(xa, ya, label='linear', color='r')
ax.add_patch(circulo)

plt.legend()
plt.show()
plt.draw()

#Los vértices de un decágono inscrito en una circunferencia de radio r son

lg=10
ag=2*pi/lg

xg1=r*cos(ag)
yg1=r*sin(ag)
xg2=r*cos(2*ag)
yg2=r*sin(2*ag)
xg3=r*cos(3*ag)
yg3=r*sin(3*ag)
xg4=r*cos(4*ag)
yg4=r*sin(4*ag)
xg5=r*cos(5*ag)
yg5=r*sin(5*ag)
xg6=r*cos(6*ag)
yg6=r*sin(6*ag)
xg7=r*cos(7*ag)
yg7=r*sin(7*ag)
xg8=r*cos(8*ag)
yg8=r*sin(8*ag)
xg9=r*cos(9*ag)
yg9=r*sin(9*ag)
xg10=r*cos(10*ag)
yg10=r*sin(10*ag)

xg=np.array([xg1,xg2,xg3,xg4,xg5,xg6,xg7,xg8,xg9,xg10,xg1])
yg=np.array([yg1,yg2,yg3,yg4,yg5,yg6,yg7,yg8,yg9,yg10,yg1])

print("""Las coordenadas de los vértices de un decágono inscrito en una circunferencia son:
v1=(%5.2f,%5.2f)
v2=(%5.2f,%5.2f)
v3=(%5.2f,%5.2f)
v4=(%5.2f,%5.2f)
v5=(%5.2f,%5.2f)
v6=(%5.2f,%5.2f)
v7=(%5.2f,%5.2f)
v8=(%5.2f,%5.2f)
v9=(%5.2f,%5.2f)
v10=(%5.2f,%5.2f)"""%(xg1,yg1,xg2,yg2,xg3,yg3,xg4,yg4,xg5,yg5,xg6,yg6,xg7,yg7,xg8,yg8,xg9,yg9,xg10,yg10))

circulo = plt.Circle((0,0), radius=r, color='b')
ax=plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

plt.gca().set_aspect('equal', adjustable='box')
plt.plot(xg, yg, label='linear', color='r')
ax.add_patch(circulo)

plt.legend()
plt.show()
plt.draw()

#Los vértices de un endecágono inscrito en una circunferencia de radio r son

ln=11
an=2*pi/ln

xn1=r*cos(an)
yn1=r*sin(an)
xn2=r*cos(2*an)
yn2=r*sin(2*an)
xn3=r*cos(3*an)
yn3=r*sin(3*an)
xn4=r*cos(4*an)
yn4=r*sin(4*an)
xn5=r*cos(5*an)
yn5=r*sin(5*an)
xn6=r*cos(6*an)
yn6=r*sin(6*an)
xn7=r*cos(7*an)
yn7=r*sin(7*an)
xn8=r*cos(8*an)
yn8=r*sin(8*an)
xn9=r*cos(9*an)
yn9=r*sin(9*an)
xn10=r*cos(10*an)
yn10=r*sin(10*an)
xn11=r*cos(11*an)
yn11=r*sin(11*an)

xn=np.array([xn1,xn2,xn3,xn4,xn5,xn6,xn7,xn8,xn9,xn10,xn11,xg1])
yn=np.array([yn1,yn2,yn3,yn4,yn5,yn6,yn7,yn8,yn9,yn10,yn11,yn1])

print("""Las coordenadas de los vértices de un endecágono inscrito en una circunferencia son:
v1=(%5.2f,%5.2f)
v2=(%5.2f,%5.2f)
v3=(%5.2f,%5.2f)
v4=(%5.2f,%5.2f)
v5=(%5.2f,%5.2f)
v6=(%5.2f,%5.2f)
v7=(%5.2f,%5.2f)
v8=(%5.2f,%5.2f)
v9=(%5.2f,%5.2f)
v10=(%5.2f,%5.2f)
v11=(%5.2f,%5.2f)"""%(xn1,yn1,xn2,yn2,xn3,yn3,xn4,yn4,xn5,yn5,xn6,yn6,xn7,yn7,xn8,yn8,xn9,yn9,xn10,yn10,xn11,yn11))

circulo = plt.Circle((0,0), radius=r, color='b')
ax=plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

plt.gca().set_aspect('equal', adjustable='box')
plt.plot(xn, yn, label='linear', color='r')
ax.add_patch(circulo)

plt.legend()
plt.show()
plt.draw()

#Los vértices de un dodecágono inscrito en una circunferencia de radio r son

ld=12
ad=2*pi/ld

xd1=r*cos(ad)
yd1=r*sin(ad)
xd2=r*cos(2*ad)
yd2=r*sin(2*ad)
xd3=r*cos(3*ad)
yd3=r*sin(3*ad)
xd4=r*cos(4*ad)
yd4=r*sin(4*ad)
xd5=r*cos(5*ad)
yd5=r*sin(5*ad)
xd6=r*cos(6*ad)
yd6=r*sin(6*ad)
xd7=r*cos(7*ad)
yd7=r*sin(7*ad)
xd8=r*cos(8*ad)
yd8=r*sin(8*ad)
xd9=r*cos(9*ad)
yd9=r*sin(9*ad)
xd10=r*cos(10*ad)
yd10=r*sin(10*ad)
xd11=r*cos(11*ad)
yd11=r*sin(11*ad)
xd12=r*cos(12*ad)
yd12=r*sin(12*ad)

xd=np.array([xd1,xd2,xd3,xd4,xd5,xd6,xd7,xd8,xd9,xd10,xd11,xd12,xd1])
yd=np.array([yd1,yd2,yd3,yd4,yd5,yd6,yd7,yd8,yd9,yd10,yd11,yd12,yd1])

print("""Las coordenadas de los vértices de un dodecágono inscrito en una circunferencia son:
v1=(%5.2f,%5.2f)
v2=(%5.2f,%5.2f)
v3=(%5.2f,%5.2f)
v4=(%5.2f,%5.2f)
v5=(%5.2f,%5.2f)
v6=(%5.2f,%5.2f)
v7=(%5.2f,%5.2f)
v8=(%5.2f,%5.2f)
v9=(%5.2f,%5.2f)
v10=(%5.2f,%5.2f)
v11=(%5.2f,%5.2f)
v12=(%5.2f,%5.2f)"""%(xd1,yd1,xd2,yd2,xd3,yd3,xd4,yd4,xd5,yd5,xd6,yd6,xd7,yd7,xd8,yd8,xd9,yd9,xd10,yd10,xd11,yd11,xd12,yd12))

circulo = plt.Circle((0,0), radius=r, color='b')
ax=plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

plt.gca().set_aspect('equal', adjustable='box')
plt.plot(xd, yd, label='linear', color='r')
ax.add_patch(circulo)

plt.legend()
plt.show()
plt.draw()
