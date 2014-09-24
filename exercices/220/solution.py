# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 22:37:07 2014

@author: Axel
"""
import is_prime
for i in range(10000, 10050):
    if is_prime.is_prime(i) == True:
        print(i, end = ', ')