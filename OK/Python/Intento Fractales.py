#!/usr/bin/python3.7
#
#David Alonso Garduño Granados
#Python(3.7.4)
#01/12/19
#01/12/19
#Fractales un intento de mi fractal
from turtle import *

def draw_fractal(length, angle, level, initial_state, target, replacement, target2, replacement2):

    state = initial_state
   
    for counter in range(level):
        state2 = ''
        for character in state:
            if character == target:
                state2 += replacement
            elif character == target2:
                state2 += replacement2
            else:
                state2 += character
        state = state2
       
    # dibujo
    for character in state:
        if character == 'F':
            forward(length)
        elif character == '+':
            right(angle)
        elif character == '-':
            left(angle)

       
if __name__ == '__main__':

    delay(0)
    speed(0)
    hideturtle()
    up(); goto(-256, 0); down();
    draw_fractal(2, 75, 6, 'FX', 'X', 'X-FX++FX-FX', '', '')
