"""
Find the Pitago List, then use it to lookup value of triplets and calculate the
max product
"""


def check_max_product_pythagore_triplet(n, pitagolist):
    """
    """
    found = 0
    maxproduct = 0
    for i in pitagolist:
        if sum(i) == n:
            found = 1
            product = i[0] * i[1] * i[2]
            if product > maxproduct:
                maxproduct = product
    if found == 0:
        return -1
    else:
        return maxproduct


if __name__ == '__main__':
    # number of test cases
    t = int(input())

    # find the pitago list where each triplet has sum <= 3000
    # assumpsion: a is the smallest, c is the biggest in triplet.
    # so a < 3000 / 3, and b < 3000 / 2.
    pitagolist = []
    for a in range(3, 1001):
        for b in range(a + 1, 1501):
            c2 = a**2 + b**2
            c = int(c2**0.5)
            if a + b + c > 3000:
                break
            if c**2 == c2:
                pitagolist.append([a, b, c])

    # each test case
    for _ in range(t):
        n = int(input())
        print(check_max_product_pythagore_triplet(n, pitagolist))
