import sys
input = sys.stdin.readline
matrix = [[0] * 58 for _ in range(58)]
M = int(input())
for _ in range(M):
    a, b = input().rstrip().split(' => ')
    a = ord(a) - 65; b = ord(b) - 65
    matrix[a][b] = 1
for k in range(58):
    for i in range(58):
        for j in range(58):
            if matrix[i][j] == 1 or (matrix[i][k] == 1 and matrix[k][j] == 1):
                matrix[i][j] = 1
cnt = 0
result = []
for i in range(58):
    matrix[i][i] = 0
for i in range(58):
    for j in range(58):
        if matrix[i][j] == 1:
            cnt += 1
            result.append((i, j))
print(cnt)
for x, y in result:
    print(f'{chr(x + 65)} => {chr(y + 65)}')
