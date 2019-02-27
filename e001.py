# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 15:28:53 2019

@author: XZentus
"""

def next_div(n, d):
    """
    return n':
        n <= n' < n + d
        n' % d == 0
    """
    if n == 0:
        return d
    if n % d == 0:
        return n
    return n + d - n % d

def prev_div(n, d):
    """
    return n':
        n - d < n' <= n
        n' % d == 0
    """
    return n - n % d

def sum_range(begin, end, div):
    """
    return sum(ns)
        ns: begin <= {n, n+d, n+2d .. n+xd} <= end
        n = next_div(begin, d)
        n+xd = prev_div(end, d)
    """
    begin = next_div(begin, div)
    end = prev_div(end, div)
    
    n_divs = 1 + (end - begin) // div
    
    if n_divs % 2 == 0:
        return begin + (n_divs - 1) * (begin + div + end) // 2
    return n_divs * (begin + end) // 2

def solve_gen(begin, end):
    (v3, v5, v15) = (sum_range(begin, end, v) for v in [3, 5, 15])
    return v3 + v5 - v15

def solve():
    return solve_gen(0, 999)