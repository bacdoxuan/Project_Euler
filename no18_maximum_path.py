import copy


class Node():
    def __init__(self, x, y, matrix):
        self.value = matrix[x][y]
        self.x = x
        self.y = y
        self.position = [x, y]
        self.current_sum = []

    def __str__(self):
        return str((self.position, self.value))

    def calculate(self, matrix_sum):
        if self.position == [0, 0]:
            self.current_sum = [[[self.value], self.value]]
        if self.y < len(matrix_sum[self.x]) - 1:
            pnode = matrix_sum[self.x - 1][self.y]
            for i in pnode.current_sum:
                j = i[0][:]
                j.append(self.value)
                totalsum = i[1] + self.value
                self.current_sum.append([j, totalsum])
        if self.y - 1 >= 0:
            pnode = matrix_sum[self.x - 1][self.y - 1]
            for i in pnode.current_sum:
                j = i[0][:]
                j.append(self.value)
                totalsum = i[1] + self.value
                self.current_sum.append([j, totalsum])


t = int(input())
for _ in range(t):
    n = int(input())
    matrix = []
    for _ in range(n):
        matrix.append([i for i in list(map(int, input().split()))])
    matrix_sum = copy.copy(matrix)

    for i in range(n):
        for j in range(i + 1):
            a = Node(i, j, matrix)
            a.calculate(matrix_sum)
            matrix_sum[i][j] = a

    maxsum = -1
    for i in range(n):
        a = matrix_sum[n - 1][i]
        for b in a.current_sum:
            c = b[1]
            if c > maxsum:
                maxsum = c

    print(maxsum)
