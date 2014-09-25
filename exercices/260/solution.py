# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 22:37:07 2014

@author: Axel
"""


import math
import numpy as np


def euclidean(a, b):
    d = sum((b - a)**2 for a, b in zip(a, b))**0.5
    print(d)
    return d

a = [2,3,7,3,4,0,8,2,1]
b = [5,3,0,7,8,6,9,4,5]
euclidean(a, b)

def opt_euclidean(a, b):
    d = math.sqrt(sum(math.pow((b - a), 2) for a, b in zip(a, b)))
    print(d)
    return d

opt_euclidean(a, b)

def np_euclidean(a, b):
    d = np.sqrt(sum(np.power((b - a), 2) for a, b in zip(a, b)))
    print(d)
    return d
np_euclidean(a, b)

