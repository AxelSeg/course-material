# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 22:37:07 2014

@author: Axel
"""
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range (0, 26):
    for j in range (0, 26):
        if alphabet[i] != alphabet[j]:
            print(alphabet[i]+alphabet[j])
        else:
            continue