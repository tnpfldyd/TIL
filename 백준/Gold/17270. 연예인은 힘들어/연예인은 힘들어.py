import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
matrix = [[INF] * N for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[a][b] = min(t, matrix[a][b])
    matrix[b][a] = min(t, matrix[b][a])
for i in range(N):
    matrix[i][i] = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                matrix[i][j] = matrix[i][k] + matrix[k][j]
j, s = map(int, input().split())
j -= 1; s -= 1
jcnt = INF
max_cnt = INF
result = []
for i in range(N):
    if i != j and i != s:
        if max_cnt > matrix[j][i] + matrix[s][i]:
            max_cnt = matrix[j][i] + matrix[s][i]
for i in range(N):
    if i != j and i != s:
        if matrix[j][i] + matrix[s][i] == max_cnt:
            if matrix[j][i] <= matrix[s][i]:
                result.append((matrix[j][i], i+1))
if len(result) == 0:
    print(-1)
else:
    result = sorted(result, key = lambda x : (x[0], x[1]))
    print(result[0][1])