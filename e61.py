# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 12:16:10 2018

@author: XZentus
"""

import itertools as iter

def octagonal(n):
    return n * (3 * n - 2)

def heptagonal(n):
    return n * (5 * n - 3) // 2

def hexagonal(n):
    return n * (2 * n - 1)

def pentagonal(n):
    return n * (3 * n - 1) // 2

def square(n):
    return n * n

def triangle(n):
    return n * (n + 1) // 2

def check_pair(n1, n2):
    return n1 % 100 == (n2 // 100) % 100

funranges = [[triangle,   45, 140],
             [square,     32, 99],
             [pentagonal, 26, 81],
             [hexagonal,  23, 70],
             [heptagonal, 21, 63],
             [octagonal,  19, 58]]

def selectn(fn, prev = None):
    if not fn:
        return
    f = fn[0]
    for i in range(*f[1:3]):
        n = f[0](i)
        if prev and not check_pair(prev, n):
            continue
        if len(fn) > 1:
            for res in selectn(fn[1:], n):
                if res:
                    yield [n] + res
        else:
            yield [n]

def solve():
    results = []
    for perm in iter.permutations(funranges):
        for result in selectn(perm):
            if check_pair(result[-1], result[0]):
                results.append(result)
    return [(sum(x), x) for x in results]