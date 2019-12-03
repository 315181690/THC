#!/usr/bin/python3.7
#
#David Alonso Garduño Granados
#Python(3.7.4)
#01/12/19
#01/12/19
#Se define una función que partiendo de un documento .txt cargue el laberinto para que python pueda trabajar con él
import sys
if len(sys.argv)==1:
    laberinto="L1.txt"
    print(sys.argv[0])
else:
    laberinto=sys.argv[1]
    print(sys.argv[1])
#print(len(sys.argv))
#print(sys.argv)
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


from prettytable import PrettyTable
p = PrettyTable()

for renglon in l:
    p.add_row(renglon)

print(p.get_string(header=False, border=False))

def avanza (L,i,j,s):
    if L[i-1][j]==0:
        L[i-1][j]=2
        s.append([i-1,j])
        avanza(L,i-1,j,s)
    elif L[i][j+1]==0:
         L[i][j+1]=2
        s.append([i, j+1])
        avanza(L,i,j+1,s)
        
