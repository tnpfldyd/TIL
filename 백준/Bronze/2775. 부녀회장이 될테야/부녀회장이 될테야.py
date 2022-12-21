import sys
input = sys.stdin.readline

visited = [[0] * 15 for _ in range(15)]

for i in range(15):
    visited[0][i] = i


for i in range(1, 15):
    cnt = 0
    for j in range(1, 15):
        cnt += visited[i-1][j]
        visited[i][j] = cnt
T = int(input())

for i in range(T):
    a, b = int(input()), int(input())
    print(visited[a][b])