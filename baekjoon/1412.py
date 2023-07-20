import sys
input = sys.stdin.readline

N = int(input())
matrix = [list(input().strip()) for _ in range(N)]

result = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 'Y' and matrix[j][i] == 'N':
            result[i][j] = True

for k in range(N):
    for i in range(N):
        for j in range(N):
            if result[i][k] and result[k][j]:
                result[i][j] = True

for i in range(N):
    if result[i][i]:
        print('NO')
        break
else:
    print('YES')
