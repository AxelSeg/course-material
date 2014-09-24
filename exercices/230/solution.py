# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 22:37:07 2014

@author: Axel
"""
import is_prime
import itertools
counter = itertools.count(100000000)
for i in counter:
    if is_prime.is_prime(i) == True:
        print(i)
        break