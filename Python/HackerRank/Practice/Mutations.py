#!/usr/bin/python3.7
#
#David Alonso Garduño Granados
#Python(3.7.4)
#01/12/19
#01/12/19
def mutate_string(string, position, character):
    list2=list(string)
    list2[position]=character      
    return ''.join(list2)
if __name__ == '__main__':
