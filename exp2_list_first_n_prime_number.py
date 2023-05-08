"""List of first n prime number."""


def find_first_n_prime(n):
    """
    Use Sieve of Eratosthenes to generate a list of first n prime numbers
    """
    list_prime = [2, 3]
    a = list_prime[-1]

    while len(list_prime) < n:
        a += 2
        b = int(a**0.5) + 1
        isprime = True
        for i in list_prime:
            if i > b:
                break
            if a % i == 0:
                isprime = False
                break
        if isprime is True:
            list_prime.append(a)
    return list_prime
