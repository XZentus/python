# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 10:55:07 2018

@author: XZentus
"""

from math import log10

from sieve import Sieve

limit = 10000

sieve = Sieve(100000000)

def concat_nums(n1, n2):
    return n1 * 10**(1 + int(log10(n2))) + n2

def check_pair(n1, n2, sieve = sieve):
    is_prime = sieve.is_prime
    return is_prime(concat_nums(n1, n2)) and is_prime(concat_nums(n2, n1))

def check_collect(lst, elements_to_add):
    
    next_prime = sieve.next_prime
    is_prime = sieve.is_prime
    
    if elements_to_add == 0:
        return lst, sum(lst)
    
    if lst and lst[0] > limit:
        return False
    
    np = None
    
    if lst:
        np = next_prime(lst[-1])
    else:
        np = 2
    
    while np < limit:
        for p in lst:
            if not check_pair(p, np):
                break
        else:
            res = check_collect([np] + lst, elements_to_add - 1)
            if res:
                return res
        
        np = next_prime(np)
        
    return False
                