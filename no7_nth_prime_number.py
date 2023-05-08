"""https://www.hackerrank.com/contests/projecteuler/challenges/euler007.

1) Check if a number is prime number
2) Go through all integer number and find prime numbers, until the number of 
prime number reach n
3) Print the value
This method we do not have to store any list of prime numbers.
"""


def isprime(a):
    counter = 0
    if a == 1:
        return False
    if a in [2, 3, 5, 7, 11]:
        return True
    if a % 6 not in [1, 5]:
        return False
    b = int(a**0.5) + 1
    c = 6 * counter + 1
    d = 6 * counter + 5
    while c < b or d < b:
        if (c != 1 and a % c == 0) or (a % d == 0):
            return False
        counter += 1
        c = 6 * counter + 1
        d = 6 * counter + 5
    return True


def find_the_n_prime(n):
    if n == 1:
        return 2
    counter = 2
    number = 3
    while True:
        if isprime(number):
            counter += 1
            if counter > n:
                return number
                break
        number += 2


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(find_the_n_prime(n))
