"""https://www.hackerrank.com/contests/projecteuler/challenges/euler005."""
import math
from collections import Counter


"""
NOTE1:
This is an upgrade version of problem no3 - Largest prime factor.
This code find all prime factors of an integer number and put them in a list,
no duplite. 
---Using recursive coding.---

NOTE2:
How to calculate the smallest multiple number:
01 = 1^1
02 =     2^1
03 =         3^1
04 =     2^2
05 =             5^1
06 =     2^1 3^1
07 =                 7^1
08 =     2^3
09 =         3^2
10 =     2^1     5^1
11 =                     11^1
12 =     2^2 3^1
13 =                          13^1
14 =     2^1         7^1
15 =         3^1 5^1
16 =     2^4
17 =                               17^1
18 =     2^1 3^2
19 =                                    19^1
20 =     2^2     5^1
--------------------------------------------
   &#8594; 1^1 2^4 3^2 5^1 7^1 11^1 13^1 17^1 19^1
Compute the prime factorization of each number from 1 to 20, and multiply the 
greatest power of each prime together
(1^1) * (2^4) * (3^2) * (5^1) * (7^1) * (11^1) * (13^1) * (17^1) * (19^1) = 232,792,560
"""  # NOQA


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


def find_smallest_multiple(n):
    result = 1
    dict_counter = {}
    for i in range(2, n + 1):
        ct = Counter(findlistprimefactor(i))
        for j in ct:
            if j not in dict_counter:
                dict_counter[j] = ct[j]
            else:
                if ct[j] > dict_counter[j]:
                    dict_counter[j] = ct[j]

    for x, y in dict_counter.items():
        result *= x**y

    return result


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        a = int(input())
        print(find_smallest_multiple(a))
