#David Alonso Garduño Granados
#29/10/19
#
#Evaluación práctica
"""Definiré la función basado en el trabajo anterior, generalizando para mayores a 2 un mínimo de 7 tríangulos para encontrar la raíz cuadrada con este método, ya que el uno solo requiere un cuadrado"""
def raiz(b):
    '''Regresa la raíz cuadrada de un número usando el area de un rectángulo, hasta convertirla en un cuadrado'''
    bases=[]
    alturas=[]
    x=b
    h=1
    print("________________________________________________")
    print("La raíz cuadrada de %g puede ser encontrada con:"%(b))
    print("|rectangulo   |   base    |   altura   |")
    print("|      1      |   %5.4f   |   %5.4f    |"%(b,h))
    for i in range(2,9):
        b=(b+h)/2
        h=x/b
        bases.append(b)
        alturas.append(h)
        print("|      %g      |   %5.4f   |   %5.4f    |"%(i,b,h))
