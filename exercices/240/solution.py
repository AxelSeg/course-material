# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 22:37:07 2014

@author: Axel
"""
def fib(n):
    a, b = 1, 2
    for i in range(n):
        a, b = b, a + b
    return a

for n in range(0, 10):
    fib(n)
    print(fib(n))