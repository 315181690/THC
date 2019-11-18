def lel(r):
    if 1<=r<=5:
        return("Patient has bright red face")
    if 6<=r<=12:
        return("Patient is unable to speak")
    if 13<=r<=20:
        return("Patient's sides are mildly bruised")
    if 21<=r<=30:
        return("Patient has broken jaw, fractured ribs")
    if 31<=r<=49:
        return("Patient is in a coma")
    if r<=50:
        return("Patient is dead")
n=input()
e=n.count('lol')
o=3*(n.count('lel'))
m=4*(n.count('lmao'))
z=2*(n.count('rofl'))
r=e+o+m+z
print(lel(r))
