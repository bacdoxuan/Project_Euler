"""https://www.hackerrank.com/contests/projecteuler/challenges/euler001."""

"""
Solution:

1)Find the sum of all number which % 3 = 0 below n:

find the number of (numbers % 3 == 0): (n - 1) // 3
the first number: 3
the last number: ((n - 1) // 3) * 3
average of first and last number: (3 + ((n - 1) // 3) * 3) / 2
to find the sum: average * the number of (numbers % 3 == 0), which is:
((3 + ((n - 1) // 3) * 3) / 2) * (n - 1 // 3)
but, to avoid using float number, we use / 2 at the last calculation, and 
replace it with //: ((((n - 1) // 3) * 3 + 3) * ((n - 1) // 3)) // 2

2) Continue like this to find the sum of all number which % 5 = 0 below n:
((((n - 1) // 5) * 5 + 5) * ((n - 1) // 5)) // 2

3) Number that % 3 == 0 and % 5 == 0 are repeated, so we have to minus those
by finding the sum of all number % 15 == 0.
((((n - 1) // 15) * 15 + 15) * ((n - 1) // 15)) // 2

4) Finally, the result is 1) + 2) - 3)

"""


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        sum_three = ((((n - 1) // 3) * 3 + 3) * ((n - 1) // 3)) // 2
        sum_five = ((((n - 1) // 5) * 5 + 5) * ((n - 1) // 5)) // 2
        sum_fifteen = ((((n - 1) // 15) * 15 + 15) * ((n - 1) // 15)) // 2
        result = sum_three + sum_five - sum_fifteen
        print(result)
