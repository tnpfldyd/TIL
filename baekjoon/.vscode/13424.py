import sys
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]
for k in range(N):
    for x in range(N):
        for y in range(N):
            matrix[x][y] = min(matrix[x][y], matrix[x][k] + matrix[k][y])
for i in range(M):
    a, b, t = map(int, input().split())
    if matrix[a-1][b-1] <= t:
        print('Enjoy other party')
    else:
        print('Stay here')
