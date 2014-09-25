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


def opt_euclidean(a, b):
    d = math.sqrt(sum(math.pow((b - a), 2) for a, b in zip(a, b)))
    print(d)
    return d


def np_euclidean(a, b):
    d = np.sqrt(sum(np.power((b - a), 2) for a, b in zip(a, b)))
    print(d)
    return d
