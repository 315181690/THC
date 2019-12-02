#!/usr/bin/python3.7
#
#David Alonso Garduño Granados
#Python(3.7.4)
#01/12/19
#01/12/19
dictionary={}
n = int(input())
for i in range(n):
    name = input()
    grade = float(input())
    dictionary[name]=grade
    
v = dictionary.values()

second=sorted(list(set(v)))[1]
secondlowest = []

for key,value in dictionary.items():
    if value == second:
        secondlowest.append(key)

secondlowest.sort()

for i in secondlowest:
    print(i)
