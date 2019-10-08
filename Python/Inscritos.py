#Jijón Romero Carolina 
#
#
#
#
#Coordenadas de los poligonos inscritas en una circunferencia de radio r 
# Las coordenadas de los vertices de un triángulo inscrito en una circunferencia de radio r
from math import sin
from math import cos
from math import pi
"definimos r como 1"
r=1
y1=r*sin(2*pi/3)
x1=r*cos(2*pi/3)
y2=r*sin(4*pi/3)
x2=r*cos(4*pi/3)
y3=r*sin(0)
x3=r*cos(0)
print("""Las coordenadas de los vértices de un triángulo de radio r son
v1=(%g,%g)
v2=(%g,%g)
v3=(%g,%g)""" %(x1,y1,x2,y2,x3,y3))

#Las coordenadas de los vértices de un cuadrado inscrito en una circunferencia de radio "r" son

xc1=r*cos(pi/2)
yc1=r*sin(pi/2)
xc2=r*cos(pi)
yc2=r*sin(pi)
xc3=r*cos(3*pi/2)
yc3=r*sin(3*pi/2)
xc4=r*cos(0)
yc4=r*sin(0)
print("""\nlas coordenadas de los vértices de un cuadrado inscrito en una circuferencia de radio r son
v1=(%g,%g)
v2=(%g,%g)
v3=(%g,%g)
v4=(%g,%g)"""%(xc1,yc1,xc2,yc2,xc3,yc3,xc4,yc4))

#Las coordenadas de los vértices de un pentágono inscrito en una circunferencia de radio r son

xp1=r*cos(2*pi/5)
yp1=r*sin(2*pi/5)
xp2=r*cos(4*pi/5)
yp2=r*sin(4*pi/5)
xp3=r*cos(6*pi/5)
yp3=r*sin(6*pi/5)
xp4=r*cos(8*pi/5)
yp4=r*sin(8*pi/5)
xp5=r*cos(0)
yp5=r*sin(0)
print("""\nlas coordenadas de un pentágono inscrito en una circuferencia de radio r son
v1=(%g,%g)
v2=(%g,%g)
v3=(%g,%g)
v4=(%g,%g) 
v5=(%g,%g)"""%(xp1,yp1,xp2,yp2,xp3,yp3,xp4,yp4,xp5,yp5))

#Las coordenadas de los vértices de un hexágono inscrito en una circuferencia de radio r son

xh1=r*cos(pi/3)
yh1=r*sin(pi/3)
xh2=r*cos(2*pi/3)
yh2=r*sin(2*pi/3)
xh3=r*cos(pi)
yh3=r*sin(pi)
xh4=r*cos(4*pi/3)
yh4=r*sin(4*pi/3)
xh5=r*cos(5*pi/3)
yh5=r*sin(5*pi/3)
xh6=r*cos(0)
yh6=r*sin(0)
print("""\nlas coordenadas de un hexágono inscrito en una circunferencia de radio r son
v1=(%g,%g)
v2=(%g,%g)
v3=(%g,%g)
v4=(%g,%g)
v5=(%g,%g)
v6=(%g,%g)"""%(xh1,yh1,xh2,yh2,xh3,yh3,xh4,yh4,xh5,yh5,xh6,yh6))


#Las coordenadas de los vértices de un heptágono inscrito en una circunferencia de radio r son


xe1=r*cos(2*pi/7)
ye1=r*sin(2*pi/7)
xe2=r*cos(4*pi/7)
ye2=r*sin(4*pi/7)
xe3=r*cos(6*pi/7)
ye3=r*sin(6*pi/7)
xe4=r*cos(8*pi/7)
ye4=r*sin(8*pi/7)
xe5=r*cos(10*pi/7)
ye5=r*sin(10*pi/7)
xe6=r*cos(12*pi/7)
ye6=r*sin(12*pi/7)
xe7=x3
ye7=y3
print("""\nlas coordenadas de un heptágono inscrito en una circunferencia de radio r son:
v1=(%g,%g)
v2=(%g,%g)
v3=(%g,%g)
v4=(%g,%g)
v5=(%g,%g)
v6=(%g,%g)
v7=(%g,%g)"""%(xe1,ye1,xe2,ye2,xe3,ye3,xe4,ye4,xe5,ye5,xe6,ye6,xe7,ye7))

#Las coordenadas de un octagono inscrito en una circunferencia de radio r son :

xo1=r*cos(pi/4)
yo1=r*sin(pi/4)
xo2=r*cos(pi/2)
yo2=r*sin(pi/2)
xo3=r*cos(3*pi/4)
yo3=r*sin(3*pi/4)
xo4=r*cos(pi)
yo4=r*sin(pi)
xo5=r*cos(5*pi/4)
yo5=r*sin(6*pi/4)
xo6=r*cos(3*pi/2)
yo6=r*sin(3*pi/2)
xo7=r*sin(7*pi/4)
yo7=r*sin(7*pi/4)
xo8=r*cos(2*pi)
yo8=r*sin(2*pi)
print("""\nlas coordenadas de un octágono inscrito en una circunferencia de radio r son:
v1=(%g,%g)
v2=(%g,%g)
v3=(%g,%g)
v4=(%g,%g)
v5=(%g,%g)
v6=(%g,%g)
v7=(%g,%g)
v8=(%g,%g)"""%(xo1,yo1,xo2,yo2,xo3,yo3,xo4,yo4,xo5,yo5,xo6,yo6,xo7,yo7,xo8,xo8))

#Las coordenadas de un eneagono inscrito en una circunferencia de radio r son :

xl1=r*cos(2*pi/9)
yl1=r*sin(2*pi/9)
xl2=r*cos(4*pi/9)
yl2=r*sin(4*pi/9)
xl3=r*cos(2*pi/3)
yl3=r*sin(2*pi/3)
xl4=r*cos(8*pi/9)
yl4=r*sin(8*pi/9)
xl5=r*cos(10*pi/9)
yl5=r*sin(10*pi/9)
xl6=r*cos(4*pi/3)
yl6=r*sin(4*pi/3)
xl7=r*sin(14*pi/9)
yl7=r*sin(14*pi/9)
xl8=r*cos(16*pi/9)
yl8=r*sin(16*pi/9)
xl9=r*cos(0)
yl9=r*sin(0)
print("""\nlas coordenadas de un eneágono inscrito en una circunferencia de radio r son:
v1=(%g,%g)
v2=(%g,%g)
v3=(%g,%g)
v4=(%g,%g)
v5=(%g,%g)
v6=(%g,%g)
v7=(%g,%g)
v8=(%g,%g)
v9=(g%,g%)"""%(xl1,yl1,xl2,yl2,xl3,yl3,xl4,yl4,xl5,yl5,xl6,yl6,xl7,yl7,xl8,yl8,xl9,yl9))


