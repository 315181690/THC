#!/usr/bin/python3.7
#
#David Alonso Garduño Granados
#Python(3.7.4)
#01/12/19
#01/12/19
#Se muestra el problema de las torres de Hanoi
def moverTorre(altura,origen, destino, intermedio):
    if altura >= 1:
        moverTorre(altura-1,origen,intermedio,destino)
        moverDisco(origen,destino)
        moverTorre(altura-1,intermedio,destino,origen)
def moverDisco(desde,hacia):
    print("mover disco de",desde,"a",hacia)
moverTorre(3,"A","B","C")
