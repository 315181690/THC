# Figuras geométricas
#
#
#
#Las coordenadas de un triangulo de lado 2 sabiendo que uno de sus vertices en el origen y su lados està sobre el eje de las x, y su lado es 2.
from math import sqrt
A=0
B=2
t = sqrt(-((B/2)**2)+(B**2))
C=1
print("""triángulo eq de lado
2 con un vértice en el
origen en el cuadrante I
y un lado sobre el eje
de las x.
Las coordenadas del triángulo son:
A=(%g,%g)
B=(%g,%g)
C=(%g,%g)"""%(A,A,B,A,C,t))

# Las coordenadas de un cuadrado de lado 2 sabiendo que uno de sus vertices en el origen y su lados està sobre el eje de las x.

ax=A
ay=A
bx=B
by=A
cx=ax+by
cy=bx+ay
dy=B
dx=B
print("""Cuadrado de lado
2 con un vértice en el
origen en el cuadrante I
y un lado sobre el eje
de las x.
Las coordenadas del cuadrado son
A=(%g,%g)
B=(%g,%g)
C=(%g,%g)
D=(%g,%g)"""%(ax,ay,bx,ax,cx,cy,dx,dy))

# las coordenadas de un rectángulo de lado 2 sabiendo que uno de sus vertices en el origen y su lado está sobre el eje de las x, y su lado es 2.

bx=6
dx=6
print("""Rectángulo de lado
2 con un vértice en el
origen en el cuadrante I
y un lado sobre el eje
de las x.
A=(%g,%g)
B=(%g,%g)
C=(%g,%g)
D(%g,%g)"""%(ax,ay,bx,by,cx,cy,dx,dy))

# las coordenadas de un paralelogramo de base 2, con uno de sus vertices en el origen y su base en eje de las x.

ax=A
ay=A
bx=B
by=A
cx=B
cy=B
dx=bx+bx
dy=cy
print("""Paralelogramo de lado
2 con un vértice en el
origen en el cuadrante I
y un lado sobre el eje
de las x.
Las coordenadas del paralelogramo son:
A=(%g,%g)
B=(%g,%g)
C=(%g,%g)
D=(%g,%g)"""%(ax,ay,bx,by,cx,cy,dx,dy))
