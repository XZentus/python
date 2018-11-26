def is_pal(n):
    s = str(n)
    return s == s[::-1]

def rev_add(a):
    t = a
    b = 0
    while a > 0:
        b = b * 10 + a % 10
        a = a // 10
    return b + t

def is_lychrel(n):
    n = rev_add(n)
    for _ in range(50):
        if is_pal(n):
            return False
        n = rev_add(n)
    return True

def solve():
    result = 0
    for i in range(1, 10000):
        result += is_lychrel(i)
    return result
