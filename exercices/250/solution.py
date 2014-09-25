# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 22:37:07 2014

@author: Axel
"""
import numpy as np
def draw_n_squares(n):
    hor = '+---'
    ver = '|   '
    plus = '+'
    for i in range(n):
        print(hor * n + plus), print(ver * (n+1))
    print(hor * n + plus)

    
draw_n_squares(5)
#def draw_n_squares(n):
#    a = '+'
#    b = '-'
#    c = '|'
#    d = ' '
#    for i in range(n):
#        for j in range()
#        vertical = (3 * n) - (n - 1)
#        horizontal = (5 * n) - (n - 1)
#    print(vertical)
#    print(horizontal)
        
#draw_n_squares(5)
