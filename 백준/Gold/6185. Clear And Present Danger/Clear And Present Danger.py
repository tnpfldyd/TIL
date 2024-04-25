import sys
input = sys.stdin.readline
N, M = map(int, input().split())
load = [int(input()) - 1 for _ in range(M)]
matrix = [list(map(int, input().split())) for _ in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
result = 0
for i in range(M - 1):
    cur, nxt = load[i], load[i + 1]
    result += matrix[cur][nxt]
    
print(result)