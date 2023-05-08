"""List of prime numbers below n."""


def list_prime_number_below_n(n):
    """
    Use Sieve of Eratosthenes to generate a list of prime numbers below n
    This method is slow.
    """
    list_prime = [2, 3]
    a = list_prime[-1]

    while True:
        a += 2
        if a > n:
            break
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


# This is another way that faster 4x than above. Test with n = 10**6, this way
# took 0.4 second, and the method above took 1.6 second


def list_prime_numbers_below_n(n):
    l = [True] * (n + 1)
    l[0] = l[1] = False
    l[2] = l[3] = True
    list_prime = []
    for i in range(2, (n // 2) + 1):
        if l[i] is True:
            list_prime.append(i)
            m = n // i
            for j in range(2, m + 1):
                l[i * j] = False

    for i in range((n // 2) + 1, n + 1):
        if l[i] is True:
            list_prime.append(i)

    return list_prime


# Optimize again, runtime is 0.3 s for generating prime numbers list below 10^6
# by removing // and * , replace it by +

def list_prime_numbers_below_or_equal(n):
    # start = time.time()
    l = [True] * (n + 1)
    l[0] = l[1] = False
    list_prime = []
    for i in range(2, (n // 2) + 1):
        if l[i] is True:
            list_prime.append(i)
            for j in range(2 * i, n + 1, i):
                l[j] = False

    for i in range((n // 2) + 1, n + 1):
        if l[i] is True:
            list_prime.append(i)
    # print(time.time() - start)
    return list_prime
