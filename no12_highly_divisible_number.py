"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler012/problem.

List prime factors is really good speed, but with large number of n, the number
of calculation is huge, so we need to speed up the searching by adding some
index point with known value.

"""
from collections import Counter


def findlistprimefactor(n):
    i = 2
    listprimefactor = []
    while i**2 <= n:
        while n % i == 0:
            n = n / i
            listprimefactor.append(i)
        i = i + 1
    if n > 1:
        listprimefactor.append(int(n))
    return listprimefactor


def number_no_divisors_greatter_then(n):
    if n == 1:
        return 3

    # with known value of n and the smallest number which has no divisors 
    # greater than n, we seperate to several point of starting to reduce the
    # number of calculations.
    # The more index added, the faster the search is
    if n < 100:
        numbertocheck = 0
        startpoint = 1
    elif n < 200:
        numbertocheck = 73536
        startpoint = 384
    elif n < 300:
        numbertocheck = 2029105
        startpoint = 2015
    elif n < 400:
        numbertocheck = 2160081
        startpoint = 2079
    elif n < 500:
        numbertocheck = 17901136
        startpoint = 5984
    elif n < 600:
        numbertocheck = 76564125
        startpoint = 12375
    elif n < 700:
        numbertocheck = 103658401
        startpoint = 14399
    elif n < 800:
        numbertocheck = 236194245
        startpoint = 21735
    else:
        numbertocheck = 842120280
        startpoint = 41040

    for i in range(startpoint, 10**12):
        no_divisors = 1
        numbertocheck += i
        if numbertocheck % 2 != 0:
            continue
        primefactors = findlistprimefactor(numbertocheck)
        counter = Counter(primefactors)
        for j, k in counter.items():
            no_divisors *= (k + 1)
        if no_divisors > n:
            return numbertocheck
            break


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(number_no_divisors_greatter_then(n))


if __name__ == '__main__':
    main()
