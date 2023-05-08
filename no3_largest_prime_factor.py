"""https://www.hackerrank.com/contests/projecteuler/challenges/euler003."""
import math
"""
Solution:
Base on the solution on this link:
http://www.mathsisfun.com/numbers/factors-all-tool.html

There are many ways to check if an integer is a prime number, and finding prime
factor list of number.

But here, we use a simple solution, that is to check if a factor is a prime
number and find the max value of all.
"""


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


def findmaxprimefactor(a):
    listprimefactor = []
    for i in range(1, math.ceil(math.sqrt(a)) + 1):
        if a % i == 0:
            if isprime(i):
                listprimefactor.append(i)
            b = int(a / i)
            if isprime(b):
                listprimefactor.append(b)
    print(max(listprimefactor))


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        a = int(input())
        findmaxprimefactor(a)
