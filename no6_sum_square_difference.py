"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler006/problem.

Find result of:
(1 + 2 + 3 + ... + n)**2 - (1**2 + 2**2 + 3**2 + ... + n**2)

Note: 1**2 + 2**2 + ... + n**2 = n*(n + 1)*(2*n + 1)
"""


if __name__ == '__main__':
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        a = sum(range(n + 1))**2
        b = n * (n + 1) * (2 * n + 1) // 6
        print(a - b)
