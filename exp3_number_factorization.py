"""Divide a number into prime factor numbers.

This method is very slow. Check another way below
"""

import math


def isprime(a):
    counter = 0
    if a == 1:
        return False
    if a in [2, 3, 5, 7, 11]:
        return True
    if a % 6 not in [1, 5]:
        return False
    b = int(a**0.5) + 1
    c = 6 * counter + 1
    d = 6 * counter + 5
    while c < b or d < b:
        if (c != 1 and a % c == 0) or (a % d == 0):
            return False
        counter += 1
        c = 6 * counter + 1
        d = 6 * counter + 5
    return True


def findlistprimefactor(a):
    if isprime(a):
        return [a]
    listprimefactor = []
    for i in range(2, math.ceil(math.sqrt(a)) + 1):
        if a % i == 0:
            if isprime(i):
                listprimefactor.append(i)
            b = int(a / i)
            if isprime(b):
                listprimefactor.append(b)
                break
            else:
                c = findlistprimefactor(b)
                for j in c:
                    listprimefactor.append(j)
                break
    return listprimefactor


"""
This method is really effective and much faster than above
"""


def findprimefactor(n):
    i = 2
    listprimefactor = []
    while i**2 <= n:
        while n % i == 0:
            n = n / i
            listprimefactor.append(i)
        i = i + 1
    if n > 1:
        listprimefactor.append(int(n))
    return listprimefactor


# With the same method, we can find the max prime factor number
def findmaxprimefactor(a):
    i = 2
    while i**2 <= a:
        while a % i == 0:
            a = a // i
        i = i + 1
    if a > 1:
        return a
    else:
        return i - 1
