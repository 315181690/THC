#David Alonso Garduño Granados
#29/10/19
#
#Evaluación práctica
"""Definimos la base del rectángulo de base "b"(depende de cada número)
y el lado = 1)"""
bases=[]
alturas=[]
b=81
x=b
h=1
print("El rectángulo número 1 tiene por base %5.4f y por altura %5.4f"%(b,h))
for i in range(2,8):
    b=(b+h)/2
    h=x/b
    bases.append(b)
    alturas.append(h)
    print("El rectángulo número %g tiene por base %5.4f y por altura %5.4f"%(i,b,h))

