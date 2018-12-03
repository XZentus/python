# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 12:54:06 2018

@author: XZentus
"""

db = dict()
    
def digits_hash(n):
    result = 0
    while n > 0:
        n, d = divmod(n, 10)
        result += 10**d
    return result

def fill_db(beg, end):
    global db
    
    db = dict()
    
    for x in range(beg, end+1):
        num = x**3
        hashnum = digits_hash(num)
        if hashnum not in db:
            db[hashnum] = []
        db[hashnum].append(x)
        
        
def solve():
    global db
    
    fill_db(100, 10000)
    
    result = 2**63
    
    for v in db.values():
        if len(v) == 5:
            result = min(result, *[x**3 for x in v])
    
    return result
            