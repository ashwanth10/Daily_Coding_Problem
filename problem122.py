"""
You are given a 2-d matrix where each cell represents number of coins in that cell.
Assuming we start at matrix[0][0], and can only move right or down, find the maximum number of coins you can collect by the bottom right corner.

For example, in this matrix

0 3 1 1
2 0 0 4
1 5 3 1
The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.
"""

def input_matrix(m, n):
    matrix = []
    for x in range(1, m+1):
        row = map(int, raw_input("Enter the {} row\n".format(x)).split())
        while(len(row) != n):
            print("Enter {} elements in a row".format(n))
            row = map(int, raw_input("Enter the {} row\n".format(x)).split())
        matrix.append(row)
    return matrix

def find_max_path(matrix, m, n):
    for i in range(1, m):
        matrix[i][0] = matrix[i][0] + matrix[i-1][0]

    for i in range(1, n):
        matrix[0][i] = matrix[0][i] + matrix[0][i-1]

    for i in range(1, m):
        for j in range(1, n):
            matrix[i][j] = matrix[i][j] + max(matrix[i - 1][j], matrix[i][j - 1])

def main():
    m = int(raw_input("Enter the no. of rows?\n"))
    n = int(raw_input("Enter the no. of columns?\n"))
    matrix = input_matrix(m, n)
    find_max_path(matrix, m, n)
    print(matrix[m-1][n-1])


if __name__ == '__main__':
    main()