#!/usr/bin/python3.7
#
#David Alonso Garduño Granados
#Python(3.7.4)
#01/12/19
#01/12/19
def swap_case(s):
    a = list(s)
    b = []
    for i in a:
        if i.islower():
             b.append(i.upper())
        else:
            b.append(i.lower())
    return("".join(b))

print(swap_case(input()))
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
