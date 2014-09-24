# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 22:37:07 2014

@author: Axel
"""
import is_prime
n = 0
for i in range(0, 1000):
    if is_prime.is_prime(i) == True:
        n = n + int(i)
print(n)