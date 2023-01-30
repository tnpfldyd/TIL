import sys
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
sum_matrix = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        sum_matrix[i][j] = sum_matrix[i-1][j] + sum_matrix[i][j-1] + matrix[i-1][j-1] - sum_matrix[i-1][j-1]
for _ in range(M):
    sx, sy, ex, ey = map(int, input().split())
    answer = sum_matrix[ex][ey] - sum_matrix[sx-1][ey] - sum_matrix[ex][sy-1] + sum_matrix[sx-1][sy-1]
    print(answer)