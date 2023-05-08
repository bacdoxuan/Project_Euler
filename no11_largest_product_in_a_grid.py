"""https://www.hackerrank.com/contests/projecteuler/challenges/euler011."""


def findmaxproduct():
    """
    Find max product of 4 adjacent number in 4 ways: right, down, left_diagonal
    and right_diagonal

    It's great use of zip function to find down list, left diagonal and right
    diagonal with only one loop
    """
    grid = []
    for _ in range(20):
        row = list(map(int, input().strip().split()))
        grid.append(row)

    right_list = []
    down_list = []
    left_diagonal = []
    right_diagonal = []

    for row in range(20):
        for col in range(17):
            a = grid[row][col: col + 4]
            if 0 in a:
                continue
            if a in right_list:
                continue
            right_list.append(a)

    for i in range(17):
        down_list.extend(list(zip(grid[i], grid[i + 1], grid[i + 2], grid[i + 3])))
        left_diagonal.extend(list(zip(grid[i][3:30], grid[i + 1][2:29], grid[i + 2][1:28], grid[i + 3][0:27])))
        right_diagonal.extend(list(zip(grid[i][0:27], grid[i + 1][1:28], grid[i + 2][2:29], grid[i + 3][3:30])))

    all_list = right_list + down_list + left_diagonal + right_diagonal
    maxproduct = -1
    for i in all_list:
        product = i[0] * i[1] * i[2] * i[3]
        if product > maxproduct:
            maxproduct = product
    return maxproduct


def main():
    print(findmaxproduct())


if __name__ == '__main__':
    main()
