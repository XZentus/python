# 1_2_3_4_5_6_7_8_9_0
# 0123456789012345678

from math import sqrt

pattern = '1_2_3_4_5_6_7_8_9_0'

def check_pattern(s):
    if s[0] != '1' or s[18] != '0':
        return False
        
    o0 = ord('0')
    
    for i in range(2, 17, 2):
        if (ord(s[i]) - o0) != ((i + 2) // 2):
            return False
    return True

def solve():
    min_target, max_target = [int(pattern.replace('_', x)) for x in ['0', '9']]

    min_target, max_target = [int(sqrt(x)) for x in [ min_target, max_target]]

    for i in range(min_target, max_target + 1, 10):
        if check_pattern(str(i * i)):
            return i, i*i