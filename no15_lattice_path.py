"""https://www.hackerrank.com/contests/projecteuler/challenges/euler015."""
from math import factorial as F
"""
Solution:

The challenge is to arrange n items and m items in a row of n + m items, and 
with the condition that only go right or go down --> n and m have only one way
of arraning, so it's the combination of n items in n + m items.
The result in math:

(n + m)! / (n!)*(n+m - n)!
or
(n + m)! / (n! * m!)
"""


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        N, M = map(int, input().split())
        result = (F(N + M) // (F(N) * F(M))) % 1000000007
        print(result)
