#!/usr/bin/python3.7
#
#David Alonso Garduño Granados
#Python(3.7.4)
#01/12/19
#01/12/19
def is_leap(year):
    leap = False
    
    if year%400==0:
        leap=True
    elif year%4==0 and year%100!=0:
        leap=True

    return(leap)
