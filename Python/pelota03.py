#!/usr/bin/python3.7
#
#David Alonso Garduño Granados
#Python(3.7.4)
#01/12/19
#01/12/19
# Calcula la posición de una pelota con una velocidad inicial
# de 5 m/s y un tiempo de 0.6 segundos
# esto no es recomendable ya que se pueden generar errores de sintaxis
velocidad_inicial = 5
constante_de_gravedad = 9.81
tiempo = 0.6
Posiciòn_vertical_de_la_bola = velocidad_inicial*tiempo - .5*constante_de_gravedad*tiempo**2
print(Posiciòn_vertical_de_la_bola)
