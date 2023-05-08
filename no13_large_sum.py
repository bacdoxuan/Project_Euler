"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler013/problem
"""


def first_ten_digits():
    nolines = int(input())
    totalsum = 0
    for _ in range(nolines):
        totalsum += int(input())

    print(str(totalsum)[:10])


if __name__ == '__main__':
    first_ten_digits()
