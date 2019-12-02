#!/usr/bin/python3.7
#
#David Alonso Garduño Granados
#Python(3.7.4)
#01/12/19
#01/12/19
#Definimos regla 30 para el problema de los autómatas
n=43
l=[0]*n
l[n//2]=1
print(l)
def r30(a,i,s):
    if [a,i,s]==[1,0,0]:
        r=1
    if [a,i,s]==[0,1,0]:
        r=1
    if [a,i,s]==[0,0,1]:
        r=1
    if [a,i,s]==[0,1,1]:
        r=1
    if [a,i,s]==[0,0,0]:
        r=0
    if [a,i,s]==[1,1,0]:
        r=0
    if [a,i,s]==[1,0,1]:
        r=0
    if [a,i,s]==[1,1,1]:
        r=0
    return(r)
ne=[]
for i in range(n):
	ne.append(r30(l[i-1],l[i],l[(i+1)%n]))
l=ne.copy()
print(l)
for j in range(22):
    ne=[]
    for i in range(n):
            ne.append(r30(l[i-1],l[i],l[(i+1)%n]))
    l=ne.copy()
    print(l)
