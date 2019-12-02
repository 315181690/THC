#!/usr/bin/python3.7
#
#David Alonso Garduño Granados
#Python(3.7.4)
#01/12/19
#01/12/19
n = 43
c = []
for i in range(n):
    c.append(0)
c[n//2] = 1  #

def rule30(a,i,s):
    if [a,i,s] == [1,0,0] or [a,i,s] == [0,1,1] or [a,i,s] == [0,1,0] or [a,i,s] == [0,0,1]:
        r = 1
    else:
        r = 0
    return(r)
print(c)

ne = []
for i in range(n):
    ne.append(rule30(c[i-1],c[i],c[(i+1)%n]))

c = ne.copy()
print(c)
for g in range(n):
    ne = []
    for i in range(n):
         ne.append(rule30(c[i-1],c[i],c[(i+1)%n]))
    c = ne.copy()
    print(c)

Y = [n//2]*len(c)

import matplotlib.pyplot as pl
pl.plot(c,Y,'bs')
pl.show()
