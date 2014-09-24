# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 22:37:07 2014

@author: Axel
"""
def starts_with(value1, value2):
    if value1 == value2 + value1.replace(value2,''):
        print(True)
    else:
        print(False)
#    print(value1)
#    print(value1.replace(value2,''))
#    print(value2 + value1.replace(value2,''))
#    print(value2)
