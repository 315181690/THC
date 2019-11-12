#David Alonso Garduño Granados
#29/10/19
#
#Evaluación práctica
"""Definiré la función basado en el trabajo anterior, generalizando para mayores a 2 un mínimo de 7 tríangulos para encontrar la raíz cuadrada con este método, ya que el uno solo requiere un cuadrado"""
from MisFunciones import vabs
def raiz(b):
    '''Regresa la raíz cuadrada de un número usando el area de un rectángulo, hasta convertirla en un cuadrado'''
    bases=[]
    alturas=[]
    x=b
    h=1
    i=1
    print("________________________________________________")
    print("La raíz cuadrada de %g puede ser encontrada con:"%(b))
    print("|rectangulo   |   base    |   altura   |")
    print("|      %g      |   %5.4f   |   %5.4f    |"%(i,b,h))
    while vabs(b-h)>=0.0001:
        b=(b+h)/2
        i=i+1
        h=x/b
        #bases.append(b)
        #alturas.append(h)
        print("|      %g      |   %5.4f   |   %5.4f    |"%(i,b,h))
