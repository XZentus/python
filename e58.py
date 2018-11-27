# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 14:11:33 2018

@author: XZentus
"""

from fractions import Fraction

from math import sqrt

def dr(n):
    return n*n

def dl(n):
    return n*n - n + 1

def ul(n):
    return n*n - 2*n + 2

def ur(n):
    return n*n - 3*n + 3

def is_prime_simple(n):
    if n % 2 == 0:
        return false
        
    if n < 10:
        if n in [3, 5, 7]:
            return True
        return False
    
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    
    return True

def check_sq(size):
    return sum(is_prime_simple(f(size)) for f in [dr, dl, ul, ur])

def solve():
    limit = 50000
    primes, nums = 0, 1
    i = 3
    while True:
        ps = check_sq(i)
        primes, nums = primes + ps, nums + 4

        if i >= limit:
            print('OVERFLOW: i={}: {}/{} => {}'.format(i, primes, nums, primes/nums))
            return None
        
        if Fraction(primes, nums) < Fraction(1, 10):
            print('\n\nRESULT: i={}: {}/{} => {}'.format(i, primes, nums, primes/nums))
            return primes, nums, i
        # print('i={} => {}/{} => {}'.format(i, primes, nums, primes/nums))
        # input()
        i += 2
    return primes, nums, i
