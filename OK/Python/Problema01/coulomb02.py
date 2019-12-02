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
constante_de_coulomb = 9*10**9
carga_numero_uno = 8*10**-6
carga_numero_dos = 10*10**-6
distancia_entre_las_cargas = 4
Fuerza_de_atraccion_entre_las_cargas = constante_de_coulomb*carga_numero_uno*carga_numero_dos/distancia_entre_las_cargas**2
print(Fuerza_de_atraccion_entre_las_cargas)
'{:.6f}'.format(-9.999999999999999e-06)
'{:.6f}'.format(8e-06)
