# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 22:37:07 2014

@author: Axel
"""
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True