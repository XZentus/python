# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 14:11:33 2018

@author: XZentus
"""

from fractions import Fraction
from sieve import Sieve

def dr(n):
    return n*n

def dl(n):
    return dr(n) - n + 1

def ul(n):
    return dr(n) - 2*n + 2

def ur(n):
    return dr(n) - 3*n + 3

def check_sq(size, erast):
    return (sum(erast.is_prime(f(size)) for f in [dr, dl, ul, ur]), 4)

def solve(sieve_limit = 500000000):
    e = Sieve(sieve_limit*2)
    
    primes, nums = 0, 1
    i = 3
    while True:
        ps, ns = check_sq(i, e)
        primes, nums = primes + ps, nums + ns

        if i*i >= sieve_limit:
            print('OVERFLOW: i={}: {}/{} => {}'.format(i, primes, nums, primes/nums))
            return None
        
        if Fraction(primes, nums) < Fraction(1, 10):
            print('\n\nRESULT: i={}: {}/{} => {}'.format(i, primes, nums, primes/nums))
            return primes, nums, i
        # print('i={} => {}/{} => {}'.format(i, primes, nums, primes/nums))
        # input()
        i += 2
