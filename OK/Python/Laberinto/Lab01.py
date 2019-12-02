#!/usr/bin/python3.7
#
#David Alonso Garduño Granados
#Python(3.7.4)
#01/12/19
#01/12/19
#Se define una función que partiendo de un documento .txt cargue el laberinto para que python pueda trabajar con él
def cargaLaberinto(laberinto):
    a=open(laberinto,"r")
    l1=" "
    l=[]
    while l1:
        l1=a.readline()
        if l1:
            l1=l1.rstrip()
            l1= [int(x) for x in list(l1)]
            l.append(l1)
    return(l)

l=cargaLaberinto("Labrinto.no-cute.txt")
print(l)
