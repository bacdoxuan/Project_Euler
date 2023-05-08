"""
Fast check if a number is prime without creating the whole list.
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
