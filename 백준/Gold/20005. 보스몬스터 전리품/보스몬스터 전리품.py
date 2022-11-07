from collections import deque
import sys
input = sys.stdin.readline
N, M, P = map(int, input().split())
matrix = [list(input().strip()) for _ in range(N)]
attack = {}
for _ in range(P):
    name, dps = input().split()
    attack[ord(name)-97] = int(dps)
boss = int(input())
start = deque()
visited = [[[-1] * M for _ in range(N)] for _ in range(P)]
for i in range(N):
    for j in range(M):
        if ord(matrix[i][j])-97 in attack:
            visited[ord(matrix[i][j])-97][i][j] = 0
            start.append((ord(matrix[i][j])-97, i, j))
dx, dy = [0,0,1,-1], [1,-1,0,0]
attacker = []
last = 0
while boss > 0:
    for _ in range(len(start)):
        name, x, y = start.popleft()
        if matrix[x][y] == 'B':
            attacker.append(name)
            continue
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if matrix[nx][ny] != 'X' and visited[name][nx][ny] == -1:
                    visited[name][nx][ny] = 0
                    start.append((name, nx, ny))
    if attacker:
        for k in attacker:
            boss -= attack[k]
print(len(attacker))