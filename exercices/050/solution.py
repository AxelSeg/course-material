# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 22:37:07 2014

@author: Axel
"""
result = 0
for i in range (0, 1000):
    if i % 3 == 0 or i % 5 == 0:
        result = result + i
print(result)