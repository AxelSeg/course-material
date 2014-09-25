# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 22:37:07 2014

@author: Axel
"""
def draw_n_squares(n):
    hor = '+---'
    ver = '|   '
    plus = '+'
    for i in range(n):
        print(hor * n + plus), print(ver * (n+1))
    print(hor * n + plus)