"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler004/problem.
"""

"""
Solution:
Find all the palindrome number which are the product of two 3-digits number
go through all palindrome number and check if it < n, that's the biggest
palindrome number < n
"""

palindromelist = []
for i in range(100, 1000):
    for j in range(100, 1000):
        a = i * j
        if str(a) == str(a)[::-1] and a not in palindromelist:
            palindromelist.append(a)
length = len(palindromelist)
palindromelist.sort()


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        a = int(input())
        for i in range(length - 1, -1, -1):
            if palindromelist[i] < a:
                print(palindromelist[i])
                break
