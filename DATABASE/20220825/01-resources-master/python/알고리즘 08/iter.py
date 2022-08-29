matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 1, 2]
]

# n x m
n = len(matrix)
m = len(matrix[0])

total = 0

for row in matrix:
    total += sum(row)

print(total)

def matrix_sum(matrix):
    return sum(map(sum, matrix)) 

matrix_sum(matrix)


# for i in range(n):
#     for j in range(m):
#         total += matrix[i][j]

# print(total)

# for i in range(n):
#     for j in range(m):
#         print(matrix[i][j], end=" ")
#     print()

