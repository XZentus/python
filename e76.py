# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 16:56:17 2018

@author: XZentus
"""

def solve():
    result = [0] * 101
    result[0] = 1
    for i in range(1, 101):
        for j in range(i, 101):
            result[j] += result[j - i]
    return result[100] - 1
