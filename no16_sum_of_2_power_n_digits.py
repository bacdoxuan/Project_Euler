"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler016.
"""


t = int(input())
for _ in range(t):
    n = int(input())
    a = 2 ** n
    print(sum(int(i) for i in str(a)))