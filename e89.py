# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 14:41:36 2018

@author: XZentus
"""

import roman

import re

def fromRomanIgnoreError(s):
    """convert Roman numeral to integer"""
    if not s:
        raise InvalidRomanNumeralError('Input can not be blank')
#    if not romanNumeralPattern.search(s):
#        raise InvalidRomanNumeralError('Invalid Roman numeral: %s' % s)

    result = 0
    index = 0
    for numeral, integer in roman.romanNumeralMap:
        while s[index:index+len(numeral)] == numeral:
            result += integer
            index += len(numeral)
    return result

def solve():
    characters_saved = 0
    
    with open('p089_roman.txt', 'r') as inp:
        for line in inp:
            characters_saved += len(line) - len(roman.toRoman(fromRomanIgnoreError(line)))
    
    return characters_saved


def solve2():
    characters_saved = 0
    
    pattern = re.compile("DCCCC|LXXXX|VIIII|CCCC|XXXX|IIII")
    replacement = "kk"
    
    with open('p089_roman.txt', 'r') as inp:
        for line in inp:
            characters_saved += len(line) - len(re.sub(pattern, replacement, line))
    
    return characters_saved