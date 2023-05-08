"""https://www.hackerrank.com/contests/projecteuler/challenges/euler010."""


def list_prime_numbers_below_n(n):
    """
    1) Make a list of n True elements
    2) Use sieve of Eratosthenes to clear all non prime numbers.
    """
    if n == 2:
        return [2]
    l = [True] * (n + 1)
    l[0] = l[1] = False
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


def main():
    t = int(input())
    list_prime = list_prime_numbers_below_n(10**6)
    list_prime_sum = [2]
    leng = len(list_prime)
    for i in range(1, leng):
        list_prime_sum.append(list_prime_sum[i - 1] + list_prime[i])
    for _ in range(t):
        n = int(input())
        if n == 2:
            print(2)
            break

    # These condition below to to find the result faster, since we already know
    # the value of prime number n with a given index
    # prime number at index 10000 is 104743, at index 20000 is 224743 and so on
        if n < 104743:
            for j in range(10000, -1, -1):
                if list_prime[j] <= n:
                    print(list_prime_sum[j])
                    break
        elif n < 224743:
            for j in range(20000, -1, -1):
                if list_prime[j] <= n:
                    print(list_prime_sum[j])
                    break
        elif n < 350381:
            for j in range(30000, -1, -1):
                if list_prime[j] <= n:
                    print(list_prime_sum[j])
                    break
        elif n < 479939:
            for j in range(40000, -1, -1):
                if list_prime[j] <= n:
                    print(list_prime_sum[j])
                    break
        elif n < 611957:
            for j in range(50000, -1, -1):
                if list_prime[j] <= n:
                    print(list_prime_sum[j])
                    break
        elif n < 746777:
            for j in range(60000, -1, -1):
                if list_prime[j] <= n:
                    print(list_prime_sum[j])
                    break
        elif n < 882389:
            for j in range(70000, -1, -1):
                if list_prime[j] <= n:
                    print(list_prime_sum[j])
                    break
        else:
            for j in range(leng - 1, -1, -1):
                if list_prime[j] <= n:
                    print(list_prime_sum[j])
                    break


if __name__ == '__main__':
    main()
