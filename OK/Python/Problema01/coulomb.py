#!/usr/bin/python3.7
#
#David Alonso Garduño Granados
#Python(3.7.4)
#01/12/19
#01/12/19
# Calcula la fuerza de atracción entre dos cargas
# de 8 microcoulombs y 10 microcoulombs a 4 cm de distacnia el uno del otro
# Para la formula necesitaremos emplear la constante de coulomb (k) para la cual usaremos un valor de 9*10**9
# El resultado se arrojará en Newtons ya que es una fuerza
k = 9*10**9
'{:.6f}'.format(8e-06)
q1 = 8*10**-6
'{:.6f}'.format(-9.999999999999999e-06)
q2 = 10*10**-6
d = 4
F = k*q1*q2/d**2
print(F)
