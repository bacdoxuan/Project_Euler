"""https://www.hackerrank.com/contests/projecteuler/challenges/euler002."""
"""
Solution:
We calcalate the sum of all even fibonacci numbers while finding them to save
time.
"""


def sum_fibonacci(n):
    a = 0
    b = 1
    sumall = 0
    while b < n:
        if b % 2 == 0:
            sumall += b
        a, b = b, a + b
    return sumall


if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        print(sum_fibonacci(n))
