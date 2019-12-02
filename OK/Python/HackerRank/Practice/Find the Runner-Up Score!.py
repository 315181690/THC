#!/usr/bin/python3.7
#
#David Alonso Garduño Granados
#Python(3.7.4)
#01/12/19
#01/12/19
if __name__ == '__main__':
    newlist = []
    n = input()
    arr = input()
    arr = arr.split()
    arr = list(map(int,arr))
    winner = arr[0]
for n in arr:
    if n > winner:
        winner = n
for i in arr:
    if i < winner:
        newlist.append(i)
runnerup = newlist[0]
for k in newlist:
    if k > runnerup:
        runnerup = k


print(runnerup)
