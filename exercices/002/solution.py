# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 10:42:41 2014

@author: Axel
"""
a = ('abcdefghijklnmopqrstuvwxyz')
b = a[::-1]
#print(b)
indices = set([5,11,17,21,25])
d = print("".join(c.upper() if i in indices else c for i, c in enumerate(b)))