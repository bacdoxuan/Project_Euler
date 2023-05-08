"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler008/problem.

First we find all the k series number in n-long number, with conditions:
1 - the series does not have 0 number
2 - the series is not repetive
to reduce the number of calculations.

Second, the the product of each series and find the biggest product. It's a
basic and easy method.
"""
from functools import reduce


def find_largest_product():
    t = int(input().strip())
    for _ in range(t):
        n, k = input().strip().split(' ')
        n, k = [int(n), int(k)]
        num = input().strip()
        groupk = []
        for i in range(n - k - 1):
            a = num[i: i + k]
            if '0' in a:
                continue
            if a in groupk:
                continue
            groupk.append(a)
        if groupk == []:
            print(0)
        else:
            maxproduct = -1
            for group in groupk:
                product = reduce(lambda x, y: x * y, [int(j) for j in group])
                if product > maxproduct:
                    maxproduct = product
            print(maxproduct)


if __name__ == '__main__':
    find_largest_product()
