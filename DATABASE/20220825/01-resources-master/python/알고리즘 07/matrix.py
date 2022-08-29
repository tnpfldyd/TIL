from pprint import pprint

# for _ in range(n):
#     matrix.append([0] * m)

# n x m
# n: 행의 개수
# m: 열의 개수
n = 5
m = 5

matrix1 = [[0] * m for _ in range(n)]

pprint(matrix1)

matrix2 = [[0] * m] * n
# [[0, 0, 0, 0, 0]]

pprint(matrix2)
