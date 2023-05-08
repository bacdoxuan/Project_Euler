""""
https://www.hackerrank.com/contests/projecteuler/challenges/euler014/problem
"""
import time


def find_sequence(n):
    print(n, end=':-> ')
    count = 0
    while True:
        if n % 2 == 0:
            n = n // 2
            count += 1
            print(n, '->', end=' ')
            if n == 1:
                break
        else:
            n = 3 * n + 1
            count += 1
            print(n, '->', end=' ')
    return count


# Use recursive
def find_sequence_recursive(n):
    if n == 0 or n == 2:
        return 1
    if n == 1:
        return 3
    count = 1
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    return count + find_sequence_recursive(n)


def find_max_sequence_under(n):
    know_values = {}
    start = time.time()
    max_length = 0
    for i in range(1, n):
        temp = i
        #print(i, ': ', end=' ')
        count = 0
        while True:
            if i % 2 == 0:
                i = i // 2
                count += 1
                if i == 1:
                    break
                if i in know_values:
                    count += know_values[i]
                    break
                #print(i, '->', end=' ')
            else:
                i = 3 * i + 1
                count += 1
                #print(i, '->', end=' ')
        know_values[temp] = count
        if count >= max_length:
            max_length = count
            max_number = temp
            #print('max: ', max_number)
        #print('/n')
    #print(know_values)
    print('Run time: ', time.time() - start)
    return (max_number, max_length)


def find_list_sequence_under(n):
    know_values = {1: 3, 2: 1}
    if n == 1:
        return {0: 0}
    start = time.time()
    #max_length = 0
    for i in range(2, n):
        temp = i
        #print(i, ': ', end=' ')
        count = 0
        if i in know_values:
            continue
        else:
            while True:
                if i % 2 == 0:
                    i = i // 2
                    count += 1
                    if i == 1:
                        break
                    else:
                        if i in know_values:
                            count += know_values[i]
                            break
                    #print(i, '->', end=' ')
                else:
                    i = 3 * i + 1
                    count += 1
                    #print(i, '->', end=' ')
                    if i in know_values:
                        count += know_values[i]
                        break
            know_values[temp] = count

            while True:
                temp = temp * 2
                if temp >= n:
                    break
                else:
                    count += 1
                    know_values[temp] = count
        #print(know_values)
        #if count >= max_length:
        #    max_length = count
        #    max_number = temp
            #print('max: ', max_number)
        #print('/n')
    #print(know_values)
    print('Run time: ', time.time() - start)
    return know_values


def find_list_sequence_under_v2(n):
    know_values = {1: 3, 2: 1}
    if n == 1:
        return {0: 0}
    if n == 2:
        return {1: 3}
    if n == 3:
        return {1: 3, 2: 1}

    x = 2
    y = 1
    while True:
        x = x * 2
        if x >= n:
            break
        else:
            y += 1
            know_values[x] = y

    start = time.time()
    for i in range(3, n):
        temp = i
        count = 0
        while True:
            if i % 2 == 0:
                i = i // 2
                count += 1
                if i in know_values:
                    count += know_values[i]
                    break
            else:
                i = 3 * i + 1
                count += 1
        know_values[temp] = count

        while True:
            temp = temp * 2
            if temp >= n:
                break
            else:
                count += 1
                know_values[temp] = count
    print('Run time: ', time.time() - start)
    return know_values


def find_list_sequence_under_v3(n):
    start = time.time()
    known_value = [False] * n
    length = [0] * n
    known_value[0] = known_value[1] = True
    length[0] = 1
    length[1] = 3
    for i, known in enumerate(known_value):
        if not known:
            b = i
            count = 0
            while True:
                if b % 2 == 0:
                    b = b // 2
                    count += 1
                    if b == 1:
                        break
                    if b < n:
                        l = length[b]
                        if l != 0:
                            count += l
                            break
                else:
                    b = 3 * b + 1
                    count += 1
            length[i] = count
            known_value[i] = True
            while True:
                i *= 2
                if i >= n:
                    break
                else:
                    count += 1
                    length[i] = count
        else:
            continue
    print(time.time() - start)
    return length


def find_list_sequence_under_v4(n):
    start = time.time()
    know_values = {0: 1, 1: 3, 2: 1}
    if n == 1:
        return {0: 1}
    if n == 2:
        return {0: 1, 1: 3}
    if n == 3:
        return {0: 1, 1: 3, 2: 1}
    for i in range(n, n // 3, -1):
        if i % 2 != 0:
            seqlist = [i]
            while i not in know_values:
                if i % 2 == 0:
                    i = i // 2
                else:
                    i = 3 * i + 1
                seqlist.append(i)
            length = len(seqlist)
            for j in range(length - 1):
                if seqlist[j] <= 6000000:
                    know_values[seqlist[j]] = know_values[i] + length - j - 1
    print(time.time() - start)
    return know_values


def find_list_sequence_under_v5(n=5000000):
    start = time.time()
    know_values = {0: 1, 1: 3, 2: 1}

    for i in range(n - 1, 2, -2):
        seqlist = [i]
        while i not in know_values:
            if i % 2 == 0:
                i = i // 2
            else:
                i = 3 * i + 1
            seqlist.append(i)
        length = len(seqlist)
        for j in range(length - 1):
            if seqlist[j] <= 6000000:
                know_values[seqlist[j]] = know_values[i] + length - j - 1
    print(time.time() - start)
    return know_values



a = find_list_sequence_under_v5()
b = [0] * 6000000
for key, value in a.items():
    b[key] = value

del a
t = int(input())
for _ in range(t):
    n = int(input())
    max_length = -1
    for i in range(n - 1, 0, -1):
        c = b[i]
        if c > max_length:
            max_length = c
            max_number = i
    print(max_number)



"""
Final
"""


""" Use statistic solution """
c = [1, 2, 3, 6, 7, 9, 18, 19, 25, 27, 54, 55, 73, 97, 129, 171, 231, 235, 313, 327, 649, 654,
     655, 667, 703, 871, 1161, 2223, 2322, 2323, 2463, 2919, 3711, 6171, 10971, 13255, 17647, 
     17673, 23529, 26623, 34239, 35497, 35655, 52527, 77031, 106239, 142587, 156159, 216367, 
     230631, 410011, 511935, 626331, 837799, 1117065, 1126015, 1501353, 1564063, 1723519, 
     2298025, 3064033, 3542887, 3732423, 5649499, 6649279, 8400511, 11200681]

t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(len(c)):
        if c[i] > n:
            print(c[i-1])
            break

"""Using recursive"""
memo = [0, 1] + [0] * 5000000
result = [0, 1] + [1] * 5000000


def collatzLength(n):
    if n <= 5000000:
        res = memo[n]
        if not res: res = memo[n] = 1 + collatzLength(3*n + 1 if n % 2 else n // 2)
    else:
        res = 1 + collatzLength(3*n + 1 if n % 2 else n // 2)
    return res


for n in range(2, 5000001):
    l = collatzLength(n)
    result[n] = n if l >= memo[result[n - 1]] else result[n - 1]


for _ in range(int(input())):
    print (result[int(input())])
