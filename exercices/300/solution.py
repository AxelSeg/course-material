# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 22:37:07 2014

@author: Axel
"""


f = open('words', 'r', encoding='utf-8')
print(f.read()[0:-1], end = '')
