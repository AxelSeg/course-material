# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 22:37:07 2014

@author: Axel
"""


count = 0
f = open('words', 'r', encoding='utf-8')
for letter in f.read():
    if letter == 'e':
        count = count + 1
print(count)
