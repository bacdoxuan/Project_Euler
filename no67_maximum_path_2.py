"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler067/problem

We define each number of the matrix as a Node. Each Node has:
- position x, y: x is row number, y is column number
- value: = number
- current sum: is the maximum sum of 2 value:
 + its value and the previous Node1 maximum sum
 + its value and the previous Node2 maximum sum
So we have to begin with the Node(0, 0). This Node is the basic Node to generate
all the remaining Node in the matrix

"""
import copy


class Node():
    def __init__(self, x, y, matrix):
        self.value = matrix[x][y]
        self.x = x
        self.y = y
        self.current_sum = 0

    def calculate(self, matrix_sum):
        # The matrix start with Node 0, 0, and its sum = its value
        if self.x == self.y == 0:
            self.current_sum = self.value
        else:
            a = -1
            b = -1
            # case 1: the node on the left edge only has one previous node
            if self.y < len(matrix_sum[self.x]) - 1:
                a = matrix_sum[self.x - 1][self.y].current_sum
            # case 2: the node on the right edge onlys has one previous node
            if self.y - 1 >= 0:
                b = matrix_sum[self.x - 1][self.y - 1].current_sum
            # if a node in the middle, it will have both value a and b above
            # finally, calculate its maximum sum
            self.current_sum = max(a, b) + self.value


t = int(input())
for _ in range(t):
    n = int(input())

    # the original matrix to store numbers
    matrix = []
    for _ in range(n):
        matrix.append([i for i in list(map(int, input().split()))])

    # we create a new copy matrix from original, to store the Nodes
    matrix_sum = copy.copy(matrix)

    # we create new Node from a number and put it into the new matrix to 
    # calculate the next Node maximum sum
    for i in range(n):
        for j in range(i + 1):
            a = Node(i, j, matrix)
            a.calculate(matrix_sum)
            matrix_sum[i][j] = a

    maxsum = -1
    for i in range(n):
        j = matrix_sum[n - 1][i].current_sum
        if j > maxsum:
            maxsum = j

    print(maxsum)
