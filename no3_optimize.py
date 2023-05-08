"""https://www.hackerrank.com/contests/projecteuler/challenges/euler003."""
"""
Solution:

Continueously divide number a until it reach a**0.5, then return the remaining
of a after dividing.
"""


def findmaxprimefactor(a):
    i = 2
    while i**2 <= a:
        while a % i == 0:
            a = a // i
        i = i + 1
    if a > 1:
        print(a)
    else:
        print(i - 1)



if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        a = int(input())
        findmaxprimefactor(a)
