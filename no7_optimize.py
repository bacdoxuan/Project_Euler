def find_the_n_prime(n, list_prime):
    """
    Use Sieve of Eratosthenes to generate a list of first n prime numbers.
    Note:
    We generate this list depend on an known prime numbers list before.
    Here we start from prime number list [2,3].
    To increase the speed of finding next n prime number, we can use a bigger
    list of known prime numbers.

    Use this list of first n prime numbers to look up the value we need.
    """
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


if __name__ == '__main__':
    t = int(input())
    list_prime = [2, 3]
    for _ in range(t):
        n = int(input())
        if n > len(list_prime):
            list_prime = find_the_n_prime(n, list_prime)
        print(list_prime[n - 1])
