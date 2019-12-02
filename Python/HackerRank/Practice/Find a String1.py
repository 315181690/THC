#!/usr/bin/python3.7
#
#David Alonso Garduño Granados
#Python(3.7.4)
#01/12/19
#01/12/19
s = input()
print(bool(len([ch for ch in s if ch.isalnum()])))
print(bool(len([ch for ch in s if ch.isalpha()])))
print(bool(len([ch for ch in s if ch.isdigit()])))
print(bool(len([ch for ch in s if ch.islower()])))
print(bool(len([ch for ch in s if ch.isupper()])))
