import sys
input = sys.stdin.readline

N, M = map(int, input().split())

A = []
for _ in range(N):
    A.append(list(map(int, list(input().strip()))))

B = []
for _ in range(N):
    B.append(list(map(int, list(input().strip()))))

def flip_3x3(matrix, r, c):
    for i in range(r, r + 3):
        for j in range(c, c + 3):
            matrix[i][j] = 1 - matrix[i][j]

operations = 0

for i in range(N - 2):
    for j in range(M - 2):
        if A[i][j] != B[i][j]:
            flip_3x3(A, i, j)
            operations += 1

for i in range(N):
    for j in range(M):
        if A[i][j] != B[i][j]:
            print(-1)
            exit()

print(operations)