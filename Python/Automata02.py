n=43
c=[0]*n
c[n//2]=1
f=(c.index(1))
e=[]
for i in range(len(c)):
	if c[i]==1:
		e.append(i)
print(e)
Y=[21]*len(e)

E=[]
t=0
for j in c:
    if j==1:
        E.append(t)
    t+=1

print(E)
import matplotlib.pyplot as pl
pl.plot(e,Y,'rs')
pl.show()
