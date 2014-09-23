# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 22:37:07 2014

@author: Axel
"""
import sys
if len(sys.argv)>1:
    if sys.argv[2] == "/" and sys.argv[3] == "0":
        print("input error")        
    elif sys.argv[2] == "+":
        print(int(sys.argv[1])+int(sys.argv[3]))
    elif sys.argv[2] == "-":
        print(int(sys.argv[1])-int(sys.argv[3]))
    elif sys.argv[2] == "*":
        print(int(sys.argv[1])*int(sys.argv[3]))
    elif sys.argv[2] == "/":
        print(int(sys.argv[1])/int(sys.argv[3]))
    elif sys.argv[2] == "%":
        print(int(sys.argv[1])%int(sys.argv[3]))
    elif sys.argv[2] == "^":
        print(int(sys.argv[1])**int(sys.argv[3]))
else:
    print("usage: python3 ./solution.py a_number (an_operator +-*/%^) a_number")