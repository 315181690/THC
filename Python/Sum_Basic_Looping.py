def Sloop(x):
    if x==1:
        return(1)
    else:
        return(x+Sloop(x-1))
n=int(input())
print(Sloop(n))
